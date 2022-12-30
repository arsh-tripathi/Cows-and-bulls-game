import tkinter as tk
import cows_and_bulls
from random import randint

# Introducing the variables
number = [0] * 4
turns = 0
win = False
validity_length = False
validity_numeric = False
nos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
bulls = 0
cows = 0

# Generating a random number

while (number[0] == number[1] or number[0] == number[2] or number[0] == number[3] or number[1] == number[2] or number[1] == number[3] or number[2] == number[3]):
    number[0] = randint(1, 9)
    number[1] = randint(0, 9)
    number[2] = randint(0, 9)
    number[3] = randint(0, 9)
num_int = 1000 * number[0] + 100 * number[1] + 10 * number[2] + number[3]
numbers = list(str(num_int))


# Starting the screen
home_screen = tk.Tk()

# Starting the game screen


def game_screen():
    global home_screen
    home_screen.destroy()
    game_screen = tk.Tk()
    game_screen.geometry("1000x1000")
    game_screen.title("Cows and Bulls Game")
    game_screen.configure(bg="black")
    number_entry_field = tk.Entry()

    def run_game():
        global cows
        global bulls
        global turns
        global win
        entered_number = number_entry_field.get()
        number_entry_field.delete(0, 100)
        cows_and_bulls.askinput(entered_number)
    number_entry_field.pack()
    enter_number_button = tk.Button(
        text="Enter", command=run_game).pack()
    row_header_label = tk.Label(
        text="Number" + 20*" " + "Bulls" + 20*" " + "Cows", fg="white", bg="black").pack()
    game_screen.mainloop()


home_screen.title("Cows and Bullls Game")
home_screen.geometry("1000x1000")
home_screen.configure(bg="black")
bg_image_label = tk.Label().place(x=0, y=0)
welcome_label = tk.Label(
    text="Welcome to the Cows and Bulls Game", fg="white", bg="black").pack()
game_screen_button = tk.Button(
    text="Start Game", command=game_screen).pack()
home_screen.mainloop()
