from tkinter import *
import time
root=Tk()
root.title("Digital Clock")
root.geometry("400x200")

def fun():
    t=time.strftime("%H:%M:%S")
    clock.config(text=t)
    clock.after(20,fun)

clock=Label(root,font="Arial 24 bold",bg='white')
clock.grid(row=2,column=2,padx=100,pady=25)
fun()

Label(root,text="Digital Clock",font="Arial 24 bold").grid(row=0,column=2)
Label(root,text="hours  minutes  seconds  ",font="Arial 8 bold").grid(row=3,column=2)

root.mainloop()
