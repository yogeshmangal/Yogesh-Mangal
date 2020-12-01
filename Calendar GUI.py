from tkinter import *
import calendar
root=Tk()
root.geometry("600x600")
root.title("Calendar GUI")
Label(root,text=calendar.calendar(2019),font="courier 10 bold",bg='white',fg='blue',justify=LEFT).pack()
root.mainloop()
