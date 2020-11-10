from tkinter import *
root=Tk()
root.title("Sample Form")
root.geometry("644x345")

myLabel=Label(root,text="Welcome to our Travel Agency",font="comicsansms 13 bold").grid(row=0,column=2,pady=10)

name=Label(root,text="Name").grid(row=1,column=0)
phone=Label(root,text="Phone").grid(row=2,column=0)
gender=Label(root,text="Gender").grid(row=3,column=0)
age=Label(root,text="Age").grid(row=4,column=0)
payment=Label(root,text="Payment mode").grid(row=5,column=0)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
agevalue=StringVar()
paymentvalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,text=namevalue).grid(row=1,column=2)
phoneentry=Entry(root,text=phonevalue).grid(row=2,column=2)
genderentry=Entry(root,text=gendervalue).grid(row=3,column=2)
ageentry=Entry(root,text=agevalue).grid(row=4,column=2)
paymententry=Entry(root,text=paymentvalue).grid(row=5,column=2)

checkbutton=Checkbutton(root,text="Want to get your meals",variable=foodservicevalue).grid(row=6,column=2,pady=10)

def fun():
    with open("data.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),agevalue.get(),paymentvalue.get()}\n")
    print("Username is",namevalue.get())
    print("Phone no. is",phonevalue.get())
    print("Gender is",gendervalue.get())
    print("Age is",agevalue.get())
    print("Payment mode is",paymentvalue.get())


b=Button(root,text="Submit",command=fun).grid(row=7,column=2)
root.mainloop()
