import turtle
from pathlib import Path
import pandas as pd

game_on = True
BASE_DIR = Path(__file__).parent
gif_path = str(BASE_DIR / "blank_states_img.gif")

state_data = pd.read_csv(BASE_DIR / "./50_states.csv")
total_data = len(state_data.state)
states = list(state_data.state)
numbers_guessed = 0
correct_guesses = []
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
screen = turtle.Screen()
screen.setup(725, 491)
screen.tracer(0)
screen.title("Guess the States")

screen.addshape(gif_path)


turtle.shape(gif_path)


def get_mouse_click_cor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_cor)

while game_on:
    screen.update()
    answer = screen.textinput(
        title=f"{numbers_guessed}/{total_data}",
        prompt="Write the state's name: ",
    )
    answer = answer.title()
    if answer.lower() == "exit":
        missed_states = [state for state in states if state not in correct_guesses]
        missed_states = pd.DataFrame(missed_states)
        missed_states.to_csv(BASE_DIR / "./missed_states.csv")
    if answer in states and answer not in correct_guesses:
        # x_cor = int(state_data["x"][state_data.state == answer].iloc[0])
        # y_cor = int(state_data["y"][state_data.state == answer].iloc[0])
        temp_state_data = state_data[state_data.state == answer]
        x_cor = temp_state_data.x.item()
        y_cor = temp_state_data.y.item()
        writer.goto(x_cor, y_cor)
        writer.write(answer, align="center", font=("Arial", 16, "normal"))
        numbers_guessed += 1
        correct_guesses.append(answer)


turtle.mainloop()
