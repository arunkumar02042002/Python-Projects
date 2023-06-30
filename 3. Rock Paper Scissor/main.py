# Rock paper Scissor game
from tkinter import *
import random
from tkinter import messagebox

# Create the main window
win = Tk()
var = IntVar()
win.title('Rock Paper Scissor Game')
win.geometry('540x100')
win.resizable(0, 0)

# Function to play the rock-paper-scissors game
def rock_paper_scissor():
    possible_answer = ['rock', 'paper', 'scissor']
    computer_answer = random.choice(possible_answer)
    e = var.get()
    e = str(e)

    # Checking if the user has selected an option or not
    if e == "0":
        messagebox.showerror('Game', 'Please select any one option')
    else:
        # Comparing the user's choice with the computer's choice and displaying the result
        if e == '1':
            if computer_answer == 'paper':
                messagebox.showinfo(
                    "Game", "Computer wins\nComputer's answer is " + computer_answer)
            elif computer_answer == 'scissor':
                messagebox.showinfo(
                    "Game", "You win\nComputer's answer is " + computer_answer)
            else:
                messagebox.showinfo("Game", "Game Tied!")
        elif e == '2':
            if computer_answer == 'scissor':
                messagebox.showinfo(
                    "Game", "Computer wins\nComputer's answer is " + computer_answer)
            elif computer_answer == 'rock':
                messagebox.showinfo(
                    "Game", "You win\nComputer's answer is " + computer_answer)
            else:
                messagebox.showinfo("Game", "Game Tied!")
        elif e == '3':
            if computer_answer == 'rock':
                messagebox.showinfo(
                    "Game", "Computer wins\nComputer's answer is " + computer_answer)
            elif computer_answer == 'paper':
                messagebox.showinfo(
                    "Game", "You win\nComputer's answer is " + computer_answer)
            else:
                messagebox.showinfo("Game", "Game Tied!")


# GUI setup
title_lbl = Label(win, text="Rock Paper Scissor Game", font=(
    'Helvetica', 17, 'bold'), bg='skyblue', width=38)
title_lbl.pack()

# Create radio buttons for the user to select their choice
R1 = Radiobutton(win, text="Rock", value=1, width=5, bg='bisque', font=("verdana", 14, 'bold'), fg='coral1',
                 variable=var, cursor='hand2')
R1.place(x=3, y=40)

R2 = Radiobutton(win, text="Paper", value=2, width=5, bg='bisque', font=("verdana", 14, 'bold'), fg='coral1',
                 variable=var, cursor='hand2')
R2.place(x=120, y=40)

R3 = Radiobutton(win, text="Scissor", value=3, width=7, bg='bisque', font=("verdana", 14, 'bold'), fg='coral1',
                 variable=var, cursor='hand2')
R3.place(x=250, y=40)

# Create a submit button to trigger the game
tw_btn = Button(win, text="Submit", font=("verdana", 10, 'bold'), bg='khaki1', fg='coral1',
                width=10, relief=RAISED, bd=2, cursor='hand2', command=rock_paper_scissor)
tw_btn.place(x=400, y=40)

# Run the main event loop
win.mainloop()