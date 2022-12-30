from pydoc import doc
import sys
from random import randint
import tkinter as tk

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

# Defining functions

# Func for checking str length


def check_length(i):
    if len(i) == 4:
        global validity_length
        validity_length = True
    else:
        length_error_label = tk.Label(
            text="Enter a four digit number only", fg="white", bg="black").pack()

# Func for checking validity of the input


def check_validity(i):
    global validity_length
    global validity_numeric
    validity_numeric = False
    validity_length = False
    check_length(i)
    if str(i).isnumeric():
        validity_numeric = True
    else:
        numeric_error_label = tk.Label(
            text="Enter a four digit number only", fg="white", bg="black").pack()

# Func for checking if victory conditions are satisfied


def check_for_win(n):
    if n == 4:
        global win
        win = True
        print("You guessed the number")
        win_label = tk.Label(text="You guessed the number",
                             fg="white", bg="black").pack()

# Func for comparing the numbers


def check(n):
    global bulls
    bulls = 0
    global cows
    cows = 0
    global number
    n_array = list(n)
    for i in range(4):
        for j in range(4):
            if numbers[i] == n_array[j]:
                if i == j:
                    bulls = bulls + 1
                elif i != j:
                    cows = cows + 1
            else:
                ()
    row_label = tk.Label(text=str(n) + 30*" " +
                         str(bulls) + 30*" " + str(cows), fg="white", bg="black").pack()
    check_for_win(bulls)

# Asking the user for an input


def askinput(entered_number):
    global bulls
    global cows
    global turns
    if turns < 10:
        #entered_number = str(input("Please enter your number here: "))
        check_validity(entered_number)
        if validity_numeric and validity_length:
            check(entered_number)
            turns = turns + 1
    elif turns >= 10:
        lose_text = tk.Label(text="You ran out of turns",
                             fg="white", bg="black").pack()
        lose_test_2 = tk.Label(text="The number was: " +
                               str(num_int), fg="white", bg="black").pack()
