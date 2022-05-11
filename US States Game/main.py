import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
states_guessed = []
no_of_states = 50
state_list = state_data.state.to_list()
answer_state = screen.textinput(title="Guess the State.", prompt="Write a state's name.").title()

while len(states_guessed) < no_of_states:
    # for index, value in state_data["state"].items():
    #     if value == answer_state:
    #         states_guessed.append(answer_state)
    #         state_row = state_data[state_data["state"] == answer_state]
    #         current_state = state_row.to_dict()
    #         x_cor = current_state["x"][index]
    #         y_cor = current_state["y"][index]
    #
    #         writer = turtle.Turtle()
    #         writer.hideturtle()
    #         writer.penup()
    #         writer.goto(x_cor, y_cor)
    #         writer.write(f"{answer_state}", align="center", font=("Arial", 8, "bold"))

    if answer_state == "Exit":
        missing_state = [state for state in state_list if state not in states_guessed]
        m_s = pandas.DataFrame(missing_state)
        m_s.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        states_guessed.append(answer_state)
        current_state = state_data[state_data["state"] == answer_state]
        x_cor = current_state.x.item()
        y_cor = current_state.y.item()

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x_cor, y_cor)
        writer.write(f"{answer_state}", align="center", font=("Arial", 8, "bold"))

    answer_state = screen.textinput(title=f"{len(states_guessed)}/{no_of_states} states guessed.",
                                    prompt="What's another state's name?").title()