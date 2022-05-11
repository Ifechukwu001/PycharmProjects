from flask import Flask, render_template
from post import Post

blog_url = "https://api.npoint.io/ed99320662742443cc5b"

blog_post = Post(blog_url)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=blog_post.response_data)


@app.route("/post/<blog_id>")
def get_post(blog_id):
    blog_index =int(blog_id) - 1
    return render_template("post.html", data=blog_post.response_data[blog_index])


if __name__ == "__main__":
    app.run(debug=True)
