import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

all_states = data.state.to_list()
correct_state = []

while len(correct_state) != len(data):
    answer = screen.textinput(title=f"{len(correct_state)}/{len(data)} States Correct", prompt="What's another state "
                                                                                               "name?").title()
    if answer == "Exit":
        missing_states = [state for state in all_states if answer not in correct_state]
        pandas.DataFrame(missing_states).to_csv("learn.csv")
        break
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        correct_state.append(answer)
