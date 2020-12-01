from tkinter import *
import sqlite3
root=Tk()
root.geometry("300x150")
root.title("Login and Signup System")
a=Label(root,text="What do you want to do?",font="Arial 14 bold",pady=10)
a.grid(row=0,column=2,columnspan=2,padx=20)

def login():
    root.destroy()
    n=Tk()
    n.title("Login Window")
    n.geometry("344x345")
    Label(text="Enter Email and Password below:",font="arial 14 bold",padx=5,pady=10).grid(row=0,column=1,columnspan=2)
    l1=Label(n,text="Email").grid(row=1,column=1,padx=5,pady=5)
    l2=Label(n,text="Password").grid(row=2,column=1,padx=5,pady=5)

    v1=StringVar()
    v2=StringVar()

    e1=Entry(n,width=30,text=v1).grid(row=1,column=2)
    e2=Entry(n,width=30,text=v2).grid(row=2,column=2)

    def fun2():
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("Select * from test where email=? AND pssword=?",(v1.get(),v2.get()))
        data=cur.fetchall()
        conn.commit()
        conn.close()
        print(data)
        if(data!=[]):
            user_name=data[0][1]
            Label(n,text="User name found with name :"+user_name).grid(row=4,column=2)
        else:
            Label(n,text="User not found").grid(row=4,column=2)

    b=Button(n,text="Login",command=fun2,bg='grey').grid(row=3,column=2,pady=20)
def signup():
    root.destroy()
    n=Tk()
    n.title("Signup Window")
    n.geometry("344x345")
    Label(n,text="Enter the details below:",font="arial 14 bold",pady=10).grid(row=0,column=1,columnspan=2)
    l1=Label(n,text="Username").grid(row=1,column=1,padx=10,pady=5)
    l2=Label(n,text="Password").grid(row=2,column=1,padx=10,pady=5)
    l3=Label(n,text="Email").grid(row=3,column=1,padx=10,pady=5)

    v1=StringVar()
    v2=StringVar()
    v3=StringVar()

    e1=Entry(n,width=30,text=v1)
    e1.grid(row=1,column=2)
    e2=Entry(n,width=30,text=v2)
    e2.grid(row=2,column=2)
    e3=Entry(n,width=30,text=v3)
    e3.grid(row=3,column=2)

    def fun():
        conn=sqlite3.connect("data.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text, pssword text,email text)")
        cur.execute("INSERT INTO test VALUES(NULL,:A,:B,:C)",
                    {'A':e1.get(),
                     'B':e2.get(),
                     'C':e3.get()})
        # cur.execute("DELETE from test where id in(7,8,9,10)")
        # cur.execute("SELECT * from test")
        # items=cur.fetchall()
        # print(items)
        Label(n,text="Account Created").grid(row=5,column=2)
        conn.commit()
        conn.close()

    b=Button(n,text="Login",command=fun,bg='grey').grid(row=4,column=2,pady=10)



b1=Button(root,text="Login",command=login,width=15,bg='grey').grid(row=1,column=2)
b2=Button(root,text="SignUp",command=signup,width=15,bg='grey').grid(row=1,column=3)

root.mainloop()
