import turtle
import pandas
from location import Location
screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

location = Location()
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    guess_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct",
                                   prompt="What's another state in the U.S?").title()
    if guess_state == "Exit":
        unknown_states = [state for state in states if state not in guessed_states ]
        print(unknown_states)
        new_data = pandas.DataFrame(unknown_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess_state in states:
        state_data = data[data.state == guess_state]
        state_x_cor = state_data.x.item()
        state_y_cor = state_data.y.item()
        location.go_to(state_x_cor, state_y_cor, guess_state)
        guessed_states.append(guess_state)

screen.exitonclick()

# states_to_learn.csv









