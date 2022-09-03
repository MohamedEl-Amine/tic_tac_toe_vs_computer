from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import random
# mode game solo or two players ====================
def mode_game_tplayer():
    chose_window()


def mode_game_solo():
    global solo
    solo = True
    chose_window()



# make the chose O or X window
def chose_window():
    Solo.after(10, Solo.destroy())
    Two_Player.after(10, Two_Player.destroy())
    X = ttk.Button(second_window, text='O', height=4, width=8, command=X_start)
    O = ttk.Button(second_window, text='X', height=4, width=8, command=O_start)
    X.grid(row=0, column=0)
    O.grid(row=0, column=1)


# know turn of player ==============================
def your_turn_player():
    global O_turn, your_turn
    if O_turn == True:
        turn = 'your turn X'
        your_turn['text'] = turn
    elif O_turn == False:
        turn = 'your turn O'
        your_turn['text'] = turn


# O start first ===================================
def O_start():
    global O_turn
    O_turn = True
    active_all_button()
    second_window.destroy()
    your_turn_player()


def X_start():
    global O_turn
    O_turn = False
    active_all_button()
    second_window.destroy()
    your_turn_player()


def check_if_win():
    global winner, count
    # IF WINNER IS X ++++++++++++++++++++++++++++++
    if b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        disable_all_button()
        WINNER = 'THE WINNER IS X'
        your_turn['text'] = WINNER
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is X")

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        disable_all_button()
        WINNER = 'THE WINNER IS X'
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        your_turn['text'] = WINNER
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is X")
    elif b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        disable_all_button()
        WINNER = 'THE WINNER IS X'
        winner = True
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        your_turn['text'] = WINNER
        messagebox.showinfo('Tic Tac Toe', "The winner is X")
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        disable_all_button()
        WINNER = 'THE WINNER IS X'
        winner = True
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        your_turn['text'] = WINNER
        messagebox.showinfo('Tic Tac Toe', "The winner is X")
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        disable_all_button()
        WINNER = 'THE WINNER IS X'
        your_turn['text'] = WINNER
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is X")
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        disable_all_button()
        WINNER = 'THE WINNER IS X'
        your_turn['text'] = WINNER
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is X")
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        disable_all_button()
        WINNER = 'THE WINNER IS X'
        your_turn['text'] = WINNER
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is X")
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        disable_all_button()
        WINNER = 'THE WINNER IS X'
        your_turn['text'] = WINNER
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is X")
    # IF WINNER IS O ++++++++++++++++++++++++++++++
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        disable_all_button()
        WINNER = 'THE WINNER IS O'
        your_turn['text'] = WINNER
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is O")
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        disable_all_button()
        WINNER = 'THE WINNER IS O'
        your_turn['text'] = WINNER
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is O")
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        disable_all_button()
        WINNER = 'THE WINNER IS O'
        your_turn['text'] = WINNER
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is O")
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        disable_all_button()
        WINNER = 'THE WINNER IS O'
        your_turn['text'] = WINNER
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is O")
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        disable_all_button()
        WINNER = 'THE WINNER IS O'
        your_turn['text'] = WINNER
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is O")
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        disable_all_button()
        WINNER = 'THE WINNER IS O'
        your_turn['text'] = WINNER
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is O")
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        disable_all_button()
        WINNER = 'THE WINNER IS O'
        your_turn['text'] = WINNER
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is O")
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        disable_all_button()
        WINNER = 'THE WINNER IS O'
        your_turn['text'] = WINNER
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic Tac Toe', "The winner is O")

    elif winner != True and count == 9:
        tie = 'is tie'
        your_turn['text'] = tie
        disable_all_button()
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo('Tic Tac Toe', "Oh is tie, Try again")


def b_clicked(b):
    global O_turn, count, solo, b1, b2, b3, b4, b5, b6, b7, b8, b9
    check_if_win()
    if solo == False:
        if b["text"] == ' ' and O_turn == True:
            b["text"] = "X"
            O_turn = False
            your_turn_player()
            count += 1
            check_if_win()

        elif b["text"] == ' ' and O_turn == False:
            b["text"] = "O"
            O_turn = True
            your_turn_player()
            count += 1
            check_if_win()
    elif solo == True:
        button = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        if b["text"] == ' ' and O_turn == False:
            b["text"] = "O"
            O_turn = True
            your_turn_player()
            count += 1
            button.remove(b)
            check_if_win()
        elif count != 9 and O_turn == True:
            random_b = random.choice(button)
            while random_b["text"] != " ":
                button.remove(random_b)
                random_b = random.choice(button)
            random_b["text"] = "X"
            button.remove(random_b)
            count += 1
            O_turn = False
            check_if_win()
            your_turn_player()

    print(count)


# disable all button function =====================
def disable_all_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# active all button function =====================
def active_all_button():
    b1.config(state=ACTIVE)
    b2.config(state=ACTIVE)
    b3.config(state=ACTIVE)
    b4.config(state=ACTIVE)
    b5.config(state=ACTIVE)
    b6.config(state=ACTIVE)
    b7.config(state=ACTIVE)
    b8.config(state=ACTIVE)
    b9.config(state=ACTIVE)


# principe window ================================
window = Tk()
window.title("Tic Tac Toe")
window.geometry("350x400")
window.minsize(280, 330)
window.maxsize(280, 330)
window.iconbitmap('TicTacToe.ico')


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, X, O, your_turn, second_window, O_turn, count, winner, Solo, Two_Player, solo
    # variable ========================================
    solo = False
    count = 0
    O_turn = None
    winner = False

    your_turn["text"] = ""
    # ========= before start the game =================
    second_window = Tk()
    second_window.title("chose who will start first TacTIcToe")
    second_window.maxsize(200, 100)
    second_window.minsize(200, 100)

    chose_one = Label(second_window, text='Chose who start first')
    chose_one.grid(row=2)
    Solo = ttk.Button(second_window, text='Solo', height=4, width=8, command=mode_game_solo)
    Two_Player = ttk.Button(second_window, text='Two Player', height=4, width=8, command=mode_game_tplayer)
    Solo.grid(row=0, column=0)
    Two_Player.grid(row=0, column=1)

    # Create buttons ==================================
    b1 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b1))
    b2 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b2))
    b3 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b3))

    b4 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b4))
    b5 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b5))
    b6 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b6))

    b7 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b7))
    b8 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b8))
    b9 = ttk.Button(window, text=' ', height=6, width=12, command=lambda: b_clicked(b9))

    # Grid Buttons ====================================
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    disable_all_button()
    second_window.mainloop()


your_turn = Label(window, text='')
your_turn.grid(row=3)



menu_barre = Menu(window)
reset_option = Menu(menu_barre, tearoff=0)
reset_option.add_command(label="Reset", command=reset)
menu_barre.add_cascade(label='option', menu=reset_option)
window.config(menu=menu_barre)
reset()
# End of loop ============================

window.mainloop()
