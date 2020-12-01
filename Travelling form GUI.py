from tkinter import *
root=Tk()
root.title("Sample Form")
root.geometry("644x345")
l=Label(text="Welcome to Mangal Travels",font="Arial 16 bold",pady=20).grid(row=0,column=2)

a=Label(text="Name").grid(row=2,column=1)
b=Label(text="Phone").grid(row=3,column=1)
c=Label(text="Gender").grid(row=4,column=1)
d=Label(text="Emergency Contact").grid(row=5,column=1)
e=Label(text="Payment mode").grid(row=6,column=1)

v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=IntVar()

e1=Entry(root,text=v1).grid(row=2,column=2)
e2=Entry(root,text=v2).grid(row=3,column=2)
e3=Entry(root,text=v3).grid(row=4,column=2)
e4=Entry(root,text=v4).grid(row=5,column=2)
e5=Entry(root,text=v5).grid(row=6,column=2)

f=Checkbutton(root,text="Want to get your meals",variable=v6)
f.grid(row=7,column=2,pady=20)


def fun():
    l=Label(text="Form Submitted Successfully",pady=10).grid(row=10,column=2)
    with open('data.txt','a') as f:
        data=f"""\nName: {v1.get()}
Phone: {v2.get()}
Gender:{v3.get()}
Emergency contact:{v4.get()}
Payment mode:{v5.get()}
Service: {v6.get()}\n"""
        f.write(data)


but=Button(root,text="Submit",command=fun).grid(row=8,column=2)
but2=Button(root,text="exit",command=root.destroy).grid(row=8,column=5)
root.mainloop()
