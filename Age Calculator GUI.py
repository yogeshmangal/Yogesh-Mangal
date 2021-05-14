#Age Calculator App

from tkinter import *
from PIL import Image, ImageTk
from datetime import date
root=Tk()
root.title("Age Calculator App")
root.geometry("344x445")
photo=ImageTk.PhotoImage(Image.open('Age-Calculator2.jpg'))
Label(image=photo).grid(row=0,column=3,pady=10)

Label(root,text="Name",pady=2,padx=5).grid(row=2,column=1)
Label(root,text="Year",pady=2).grid(row=3,column=1)
Label(root,text="Month",pady=2).grid(row=4,column=1)
Label(root,text="Day",pady=2).grid(row=5,column=1)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()

e1=Entry(root,text=var1)
e1.grid(row=2,column=3)
e2=Entry(root,text=var2)
e2.grid(row=3,column=3)
e3=Entry(root,text=var3)
e3.grid(row=4,column=3)
e4=Entry(root,text=var4)
e4.grid(row=5,column=3)


def calculate_image():
    if(e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()==""):
        Label(root,text="Please fill all details",font="Arial 10 bold").grid(row=7,column=3)
    else:
        dt=date.today()
        day=int(e4.get())
        month=int(e3.get())
        year=int(e2.get())
        db=date(year,month,day)
        age=(dt-db).days//365
        top=Toplevel()
        top.title("Your Age")
        top.geometry("444x345")
        f=Frame(top,borderwidth=2,relief=SUNKEN)
        f.pack(pady=10,fill=X)
        txt="Hey "+e1.get()+"\nYour age is "+str(age)
        Label(f,text=txt,font="Arial 15 bold",bg='black',fg='white',pady=10).pack(pady=10,fill=X)

Button(root,text="Calculate Age",bg='pink',command=calculate_image).grid(row=6,column=3,pady=5)

root.mainloop()
