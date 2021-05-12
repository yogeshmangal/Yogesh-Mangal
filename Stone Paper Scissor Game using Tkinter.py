#Rock Paper Scissor Game using Tkinter

from tkinter import *
import random
L=["Rock","Paper","Scissor"]
r=random.choice(L)

root=Tk()
root.title("Rock Paper Scissor Game")
root.geometry("644x345")

def fun1():
    if(r=="Rock"):
        txt="""Your Choice: Rock
        Computer's Choice: Rock
        Game Tie"""
    elif(r=="Paper"):
        txt = """Your Choice: Rock
        Computer's Choice: Paper
        Your Score: 0
        Computer's Score: 1"""
    else:
        txt = """Your Choice: Rock
        Computer's Choice: Scissor
        Your Score: 1
        Computer's Score: 0"""

    f = Frame(root, bg='red', borderwidth=3, relief=SUNKEN)
    f.pack(pady=40)
    l = Label(f, text=txt, font="Arial 10 bold", bg='yellow', pady=30,padx=50)
    l.pack()


def fun2():
    if (r == "Paper"):
        txt = """Your Choice: Paper
            Computer's Choice: Paper
            Game Tie"""
    elif (r == "Rock"):
        txt = """Your Choice: Paper
            Computer's Choice: Rock
            Your Score: 1
            Computer's Score: 0"""
    else:
        txt = """Your Choice: Paper
            Computer's Choice: Scissor
            Your Score: 0
            Computer's Score: 1"""

    f = Frame(root, bg='red', borderwidth=3, relief=SUNKEN)
    f.pack(pady=40)
    l = Label(f, text=txt, font="Arial 10 bold", bg='yellow', pady=30, padx=50)
    l.pack()

def fun3():
    if (r == "Scissor"):
        txt = """Your Choice: Scissor
            Computer's Choice: Scissor
            Game Tie"""
    elif (r == "Paper"):
        txt = """Your Choice: Scissor
            Computer's Choice: Paper
            Your Score: 1
            Computer's Score: 0"""
    else:
        txt = """Your Choice: Scissor
            Computer's Choice: Rock
            Your Score: 0
            Computer's Score: 1"""

    f = Frame(root, bg='red', borderwidth=3, relief=SUNKEN)
    f.pack(pady=40)
    l = Label(f, text=txt, font="Arial 10 bold", bg='yellow', pady=30, padx=50)
    l.pack()

Label(root,text="Let's play the game !!",font="Arial 15 bold").pack(pady=10)
Button(root,text="Rock",bg='powder blue',pady=5,padx=20,width=10,command=fun1).pack()
Button(root,text="Paper",bg='pink',pady=5,padx=20,width=10,command=fun2).pack()
Button(root,text="Scissor",bg='pale green',pady=5,padx=20,width=10,command=fun3).pack()


mainloop()
