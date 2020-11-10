from tkinter import *
root=Tk()
root.title("Simple Calculator")

e=Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def fun(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))

def add():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="addition"
    f_num=int(first_number)

def sub():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="substratcion"
    f_num=int(first_number)

def mult():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    

def div():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="division"
    f_num=int(first_number)

def clear():
    e.delete(0,END)

def equal():
    second_number=e.get()
    e.delete(0,END)
    if(math=='addition'):
        e.insert(0,f_num+int(second_number))
    if(math=='substraction'):
        e.insert(0,f_num-int(second_number))
    if(math=='multiplication'):
        e.insert(0,f_num*int(second_number))
    if(math=='division'):
        e.insert(0,f_num/int(second_number))

b1=Button(root,text="1",padx=40,pady=20,command=lambda:fun(1))
b2=Button(root,text="2",padx=40,pady=20,command=lambda:fun(2))
b3=Button(root,text="3",padx=40,pady=20,command=lambda:fun(3))
b4=Button(root,text="4",padx=40,pady=20,command=lambda:fun(4))
b5=Button(root,text="5",padx=40,pady=20,command=lambda:fun(5))
b6=Button(root,text="6",padx=40,pady=20,command=lambda:fun(6))
b7=Button(root,text="7",padx=40,pady=20,command=lambda:fun(7))
b8=Button(root,text="8",padx=40,pady=20,command=lambda:fun(8))
b9=Button(root,text="9",padx=40,pady=20,command=lambda:fun(9))
b0=Button(root,text="0",padx=40,pady=20,command=lambda:fun(0))

b_add=Button(root,text="+",padx=40,pady=10,command=add)
b_sub=Button(root,text="-",padx=40,pady=10,command=sub)
b_mult=Button(root,text="X",padx=40,pady=10,command=mult)
b_div=Button(root,text="/",padx=40,pady=10,command=div)

b_equal=Button(root,text="=",padx=85,pady=20,command=equal)
b_clear=Button(root,text="Clear",padx=80,pady=20,command=clear)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)

b_add.grid(row=5,column=0)
b_sub.grid(row=6,column=0)
b_mult.grid(row=6,column=1)
b_div.grid(row=6,column=2)

b_equal.grid(row=4,column=1,columnspan=2)
b_clear.grid(row=5,column=1,columnspan=2)

root.mainloop()
