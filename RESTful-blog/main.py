from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["CKEDITOR_SERVE_LOCAL"] = True
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).order_by(BlogPost.id).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).order_by(BlogPost.id).all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def create_post():
    create_form = CreatePostForm()
    if create_form.validate_on_submit():
        post_title = request.form.get("title")
        print(post_title)
        post_subtitle = request.form.get("subtitle")
        post_author = request.form.get("author")
        post_img_url = request.form.get("img_url")
        post_content = request.form.get("body")
        post_date = datetime.datetime.now().strftime("%B %d, %Y")

        new_post = BlogPost(title=post_title,
                            subtitle=post_subtitle,
                            author=post_author,
                            img_url=post_img_url,
                            body=post_content,
                            date=post_date)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=create_form, page_title="New Post")


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post_edit = db.session.query(BlogPost).get(post_id)
    edit_form = CreatePostForm(title=post_edit.title,
                               subtitle=post_edit.subtitle,
                               author=post_edit.author,
                               img_url=post_edit.img_url,
                               body=post_edit.body)
    if edit_form.validate_on_submit():
        post_edit.title = request.form.get("title")
        post_edit.subtitle = request.form.get("subtitle")
        post_edit.author = request.form.get("author")
        post_edit.img_url = request.form.get("img_url")
        post_edit.body = request.form.get("body")
        db.session.commit()
        return redirect(url_for("show_post", index=post_id))
    return render_template("make-post.html", form=edit_form, page_title="Edit Post")


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_2_delete = db.session.query(BlogPost).get(post_id)
    db.session.delete(post_2_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)