from tkinter import *
root=Tk()
root.title("Currency Converter")
root.geometry("644x644")

def fun():
    if(var.get()=='Dollar'):
        #print(str(d.get()*74.19)+" Rs")
        Label(text=str(d.get())+" Dollar in INR is "+str(d.get()*74.19)+" Rs",pady=10).pack()
    elif(var.get()=='Dirham'):
        #print(str(d.get()*20.19)+" Rs")
        Label(text=str(d.get())+" Dirham in INR is "+str(d.get() * 20.19) + " Rs", pady=10).pack()
    elif(var.get()=='Ruble'):
        #print(str(d.get()*0.98)+" Rs")str(d.get())+" Dollar in INR is "+
        Label(text=str(d.get())+" Ruble in INR is "+str(d.get() * 0.98) + " Rs", pady=10).pack()
    elif(var.get()=='Pound'):
        #print(str(d.get()*98.48)+" Rs")
        Label(text=str(d.get())+" Pound in INR is "+str(d.get() * 98.48) + " Rs", pady=10).pack()

Label(text="Currency Converter",font="Arial 16 bold",pady=20).pack()
Label(text="Select the below currency to convert it into Indian Rs.").pack()
var=StringVar()
var.set("Yogesh")
r1=Radiobutton(root,text="Dollar",variable=var,value="Dollar").pack()
r2=Radiobutton(root,text="Dirham",variable=var,value="Dirham").pack()
r3=Radiobutton(root,text="Ruble",variable=var,value="Ruble").pack()
r4=Radiobutton(root,text="Pound",variable=var,value="Pound").pack()

Label(text="Enter amount:").pack(pady=10)
d=DoubleVar()
e=Entry(root,text=d).pack()
b=Button(root,text="Convert",command=fun).pack()
root.mainloop()
