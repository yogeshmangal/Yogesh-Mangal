#Bus Reservation System Project

from tkinter import *
import tkinter.messagebox as msg
import sqlite3

root=Tk()
root.title("Bus Reservation Portal")
root.geometry("1000x345")
Label(root,text="Welcome to Mangal Travels",font="Arial 14 bold",padx=50,pady=10).grid(row=0,column=1,columnspan=8)


def fun():
    new=Toplevel()
    new.title("Create Account")
    new.geometry("844x445")
    Label(new,text="Account Creation",font="times 14 bold").grid(row=0,column=2,pady=10,padx=10)
    n=Label(new,text="Name").grid(row=2,column=1,padx=30,pady=5)
    a=Label(new,text="Age").grid(row=3,column=1,padx=30,pady=5)
    m=Label(new,text="Mobile").grid(row=4,column=1,padx=30,pady=5)
    s=Label(new,text="Sex").grid(row=5,column=1,padx=30,pady=5)
    c=Label(new,text="City").grid(row=6,column=1,padx=30,pady=5)
    s=Label(new,text="State").grid(row=7,column=1,padx=30,pady=5)
    p=Label(new,text="Create Password").grid(row=8,column=1,padx=30,pady=5)

    e1=Entry(new,width=25)
    e1.grid(row=2,column=2)
    e2=Entry(new,width=25)
    e2.grid(row=3,column=2)
    e3=Entry(new,width=25)
    e3.grid(row=4,column=2)
    e4=Entry(new,width=25)
    e4.grid(row=5,column=2)
    e5=Entry(new,width=25)
    e5.grid(row=6,column=2)
    e6=Entry(new,width=25)
    e6.grid(row=7,column=2)
    e7=Entry(new,width=25)
    e7.grid(row=8,column=2)

    def create():
        conn=sqlite3.connect("Data.db")
        cur=conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS bus(
                    name text,age integer,mobile text,sex text,city text,state text,password text,
                    location text,fare integer)""")
        cur.execute("Insert into bus values(:A,:B,:C,:D,:E,:F,:G,:H,:I)",
                        {'A':e1.get(),
                         'B':e2.get(),
                         'C':e3.get(),
                         'D':e4.get(),
                         'E':e5.get(),
                         'F':e6.get(),
                         'G':e7.get(),
                         'H':None,
                         'I':None})
        cur.execute("SELECT oid,* from  bus")
        data=cur.fetchall()
        conn.commit()
        conn.close()
        Label(new,text="Congratulations!! Account Created Successfully",font="Arial 10").grid(row=10,column=2)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)

    b1=Button(new,text="Create",command=create,bg="grey",width=10).grid(row=9,column=2,pady=20)
    def dest():
        a=msg.askokcancel("Confirm Exit","Are you sure you want to exit?")
        if(a==1):
            new.destroy()
    b2=Button(new,text="Exit",command=dest,bg="grey",width=10).grid(row=9,column=3,pady=20)



def fun2():
    new=Toplevel()
    new.geometry('644x345')
    new.title("Bus Booking")
    Label(new,text="Login Details",font="Arial 14 bold").grid(row=0,column=1,pady=10,padx=20)
    n=Label(new,text="Enter Name").grid(row=1,column=0,padx=10,pady=5)
    p=Label(new,text="Enter Password").grid(row=2,column=0,padx=10,pady=5)

    v1=Entry(new,width=25)
    v1.grid(row=1,column=1)
    v2=Entry(new, width=25)
    v2.grid(row=2, column=1)

    def log():
        conn=sqlite3.connect("Data.db")
        cur=conn.cursor()
        cur.execute("Select *from bus where name=? AND password=?",(v1.get(),v2.get()))
        data=cur.fetchall()
        conn.commit()
        conn.close()
        if(data==[]):
            Label(new,text="Account not Valid").grid(row=4,column=1,pady=10)
        else:
            Label(new,text="Logged in Successfully!!").grid(row=4,column=1,pady=10)
            Label(new,text="You will redirect to Booking Portal within 5 seconds").grid(row=5,column=1,pady=10)
            d=Toplevel()
            d.title("Bus Booking Portal")
            d.geometry("644x345")
            Label(d,text="Our Destinations are:",font="Arial 16 bold",padx=80).grid(row=0,column=1,padx=30,pady=10)
            Label(d,text="A.Dholpur to Agra   : 90Rs/person",font="times 12 bold",padx=5,bg='brown').grid(row=1,column=1,padx=20,pady=5)
            Label(d,text="B.Dholpur to Delhi  : 300Rs/person",font="times 12 bold",padx=5,bg='pink').grid(row=2,column=1,padx=20,pady=5)
            Label(d,text="C.Dholpur to Murena : 80Rs/person",font="times 12 bold",padx=5,bg='red').grid(row=3,column=1,padx=20,pady=5)
            Label(d,text="Choose your Destination:",font="Arial 12 bold").grid(row=4,column=1)
            var1=StringVar()
            var1.set("Choose")
            var2=IntVar()
            P=OptionMenu(d,var1,"A","B","C").grid(row=4,column=2)
            Label(d,text="Enter the no. of Tickets:",font="Arial 12 bold").grid(row=5,column=1,pady=5)
            e=Entry(d,width=5,textvariable=var2).grid(row=5,column=2,pady=5)
            def book():
                if (var2.get() == 0 or var1.get() == "Choose"):
                    Label(d, text="Please select seat or  no. of seats first").grid(row=9, column=1)
                else:
                    a=msg.askyesno("Confirm Booking","Do you want to confirm booking?")
                    if(a==1):
                        if(var1.get()=='A'):
                            total=var2.get()*90
                            destination=str(var2.get())+" Tickets from Dholpur to Agra"
                            Label(d,text=str(var2.get())+" Tickets confirmed from Dholpur to Agra").grid(row=9,column=1)
                            Label(d,text="Total Fare is "+str(total)).grid(row=10,column=1)
                            conn=sqlite3.connect('Data.db')
                            cur=conn.cursor()
                            cur.execute("UPDATE bus set location=? where name=? and password=?",(destination,v1.get(),v2.get()))
                            cur.execute("UPDATE bus set fare=? where name=? and password=?",(total,v1.get(),v2.get()))
                            conn.commit()
                            conn.close()
                        elif(var1.get()=='B'):
                            total=var2.get()*300
                            destination= str(var2.get())+" Tickets from Dholpur to Delhi"
                            Label(d, text=str(var2.get()) + " Tickets confirmed from Dholpur to Delhi").grid(row=9, column=1)
                            Label(d, text="Total Fare is " + str(total)).grid(row=10, column=1)
                            conn = sqlite3.connect('Data.db')
                            cur = conn.cursor()
                            cur.execute("UPDATE bus set location=? where name=? and password=?",(destination, v1.get(), v2.get()))
                            cur.execute("UPDATE bus set fare=? where name=? and password=?",(total, v1.get(), v2.get()))
                            conn.commit()
                            conn.close()
                        elif(var1.get()=='C'):
                            total=var2.get()*80
                            destination = str(var2.get())+" Tickets from Dholpur to Murena"
                            Label(d, text=str(var2.get()) + " Tickets confirmed from Dholpur to Murena").grid(row=9, column=1)
                            Label(d, text="Total Fare is " + str(total)).grid(row=10, column=1)
                            conn = sqlite3.connect('Data.db')
                            cur = conn.cursor()
                            cur.execute("UPDATE bus set location=? where name=? and password=?",(destination, v1.get(), v2.get()))
                            cur.execute("UPDATE bus set fare=? where name=? and password=?",(total, v1.get(), v2.get()))
                            conn.commit()
                            conn.close()


            Button(d,text="Book",bg='grey',padx=20,command=book).grid(row=7,column=1,pady=20,ipadx=50)

    Button(new,text="Login",command=log,bg='grey',width=10).grid(row=3,column=1,pady=10)


def fun3():
    new = Toplevel()
    new.geometry('644x345')
    new.title("Payment")
    Label(new, text="Login Details", font="Arial 14 bold").grid(row=0, column=1, pady=10, padx=20)
    n = Label(new, text="Enter Name").grid(row=1, column=0, padx=10, pady=5)
    p = Label(new, text="Enter Password").grid(row=2, column=0, padx=10, pady=5)

    v1 = Entry(new, width=25)
    v1.grid(row=1, column=1)
    v2 = Entry(new, width=25)
    v2.grid(row=2, column=1)
    def paylog():
        conn = sqlite3.connect("Data.db")
        cur = conn.cursor()
        cur.execute("Select *from bus where name=? AND password=?", (v1.get(), v2.get()))
        data = cur.fetchall()
        conn.commit()
        conn.close()
        if (data == []):
            Label(new, text="Account not Valid").grid(row=4, column=1, pady=10)
        else:
            Label(new, text="Logged in Successfully!!").grid(row=4, column=1, pady=10)
            p=Toplevel()
            p.title("Payment Portal")
            p.geometry("644x545")
            conn=sqlite3.connect("Data.db")
            cur=conn.cursor()
            cur.execute("SELECT location,fare from bus where name=? and password=?",(v1.get(),v2.get()))
            data=cur.fetchall()
            conn.commit()
            conn.close()
            if(data[0][0]==None or data[0][1]==None):
                Label(p,text="You don't have any dues..Thank You!!",font="Arial 12 bold",padx=80,pady=10).grid(row=0,column=1,pady=10,padx=30)
            else:
                Label(p,text="Make Payment of "+str(data[0][1])+" Rs.only",font="Arial 16 bold", padx=80).grid(row=0,column=0,padx=30,pady=10,columnspan=2)
                Label(p, text="Payment Options are:", font="Arial 14 bold", padx=80).grid(row=1, column=0, padx=30,pady=10)
                Label(p, text="A.Paytm", font="times 12 bold", padx=5).grid(row=2,column=0,padx=20,pady=5)
                Label(p, text="B.Google Pay", font="times 12 bold", padx=5).grid(row=3,column=0,padx=20,pady=5)
                Label(p, text="C.PhonePe", font="times 12 bold", padx=5).grid(row=4,column=0,padx=20,pady=5)
                Label(p, text="D.Bhim UPI", font="times 12 bold", padx=5).grid(row=5,column=0,padx=20,pady=5)
                Label(p, text="Choose your Payment Method:", font="Arial 12 bold").grid(row=6, column=0)
                var=StringVar()
                var.set("Choose")
                P=OptionMenu(p,var,"A","B","C","D").grid(row=6, column=1)
                def pay():
                    Label(p,text="Amount Received Successfully",font="times 10 bold").grid(row=8,column=0)
                    conn=sqlite3.connect("Data.db")
                    cur=conn.cursor()
                    cur.execute("UPDATE bus set location=?,fare=? where name=? and password=?",(None,None,v1.get(),v2.get()))
                    conn.commit()
                    conn.close()
                Button(p,text="Pay",bg='grey',command=pay,width=20).grid(row=7,column=0,pady=20)

    Button(new, text="Login", command=paylog, bg='grey', width=10).grid(row=3, column=1, pady=10)

def fun4():
    new = Toplevel()
    new.geometry('644x345')
    new.title("Cancel Reservation")
    Label(new, text="Login Details for cancel Reservation", font="Arial 14 bold").grid(row=0, column=1, pady=10,padx=20)
    n = Label(new, text="Enter Name").grid(row=1, column=0, padx=10, pady=5)
    p = Label(new, text="Enter Password").grid(row=2, column=0, padx=10, pady=5)

    v1 = Entry(new, width=25)
    v1.grid(row=1, column=1)
    v2 = Entry(new, width=25)
    v2.grid(row=2, column=1)

    def cancel():
        conn=sqlite3.connect('Data.db')
        cur=conn.cursor()
        cur.execute("Select location,fare from bus where name=? and password=?",(v1.get(),v2.get()))
        data=cur.fetchall()
        if(data[0][0]==None):
            Label(new,text="This account does not have any booking").grid(row=4,column=1)
            conn.commit()
            conn.close()
        else:
            cur.execute("UPDATE bus set location=?,fare=? where name=? and password=?",(None,None,v1.get(),v2.get()))
            conn.commit()
            conn.close()
            Label(new,text="Reservation Cancelled Successfully").grid(row=4,column=1)

    Button(new, text="Cancel Reservation", command=cancel, bg='grey', width=15).grid(row=3, column=1, pady=10)



def fun5():
    acc=Toplevel()
    acc.title("Your Accounts")
    acc.geometry("644x345")
    Label(acc, text="Login Details", font="Arial 14 bold").grid(row=0, column=1, pady=10, padx=20)
    n=Label(acc, text="Enter Name").grid(row=1, column=0, padx=10, pady=5)
    p=Label(acc, text="Enter Password").grid(row=2, column=0, padx=10, pady=5)

    v1=Entry(acc, width=25)
    v1.grid(row=1, column=1)
    v2=Entry(acc, width=25)
    v2.grid(row=2, column=1)

    def login():
        conn = sqlite3.connect("Data.db")
        cur = conn.cursor()
        cur.execute("Select * from bus where name=? AND password=?", (v1.get(), v2.get()))
        data = cur.fetchall()
        conn.commit()
        conn.close()
        if(data==[]):
            Label(acc,text="Account not exists").grid(row=4,column=1)
        else:
            n=Toplevel()
            n.geometry("944x545")
            n.title("Account Details")
            Label(n,text="Your Account Details",font="times 14 bold",padx=10,pady=10).grid(row=0,column=1,padx=10,pady=10)
            for i in data:
                Label(n,text="Name:  "+str(i[0]),padx=10,pady=10).grid(row=1,column=1)
                Label(n,text="Age:  "+str(i[1]),padx=10,pady=10).grid(row=2,column=1)
                Label(n,text="Mobile:  "+str(i[2]),padx=10,pady=10).grid(row=3,column=1)
                Label(n,text="Gender:  "+str(i[3]),padx=10,pady=10).grid(row=4,column=1)
                Label(n,text="City:  "+str(i[4]),padx=10,pady=10).grid(row=5,column=1)
                Label(n,text="State:  "+str(i[5]),padx=10,pady=10).grid(row=6,column=1)
                Label(n,text="Password:  "+str(i[6]),padx=10,pady=10).grid(row=7,column=1)
                Label(n,text="Reservation Status:  "+str(i[7]),padx=10,pady=10).grid(row=8,column=1)
                Label(n,text="Fair dues:  "+str(i[8]),padx=10,pady=10).grid(row=9,column=1)

    Button(acc, text="Login", command=login, bg='grey', width=10).grid(row=3, column=1, pady=10)


def fun6():
    new=Toplevel()
    new.title("About")
    #new.geometry("600x400")
    Label(new,text="Our System:",font="Arial 16 bold",pady=10).grid(row=0,column=0)
    Label(new,text="""In the hustle and bustle of life, people have no time.
    They are so busy in their life.If they have to travel,they 
    have no time to buy tickets offline . So,there is a need of
    some online tool so that they can easily books their tickets 
    without any difficulties.The Bus Reservation Management System 
    provides you this facility. Here, you can reserve your sheet 
    and cancel at any time without any risk.""",font="Courier 14 bold",pady=10).grid(row=1,column=0)
    ib=Button(new,text="Exit",command=new.destroy,width=10,bg='grey').grid(row=3,column=0,pady=10)

def fun7():
    new = Toplevel()
    new.geometry('644x345')
    new.title("Delete Account")
    Label(new, text="Login Details for deleting the Account", font="Arial 14 bold").grid(row=0, column=1, pady=10, padx=20)
    n = Label(new, text="Enter Name").grid(row=1, column=0, padx=10, pady=5)
    p = Label(new, text="Enter Password").grid(row=2, column=0, padx=10, pady=5)

    v1 = Entry(new, width=25)
    v1.grid(row=1, column=1)
    v2 = Entry(new, width=25)
    v2.grid(row=2, column=1)

    def logs():
        conn=sqlite3.connect("Data.db")
        cur=conn.cursor()
        cur.execute("Select * from bus where name=? and password=?",(v1.get(),v2.get()))
        data=cur.fetchall()
        if(data==[]):
            Label(new,text="Account not Valid").grid(row=4,column=1)
            conn.commit()
            conn.close()
        else:
            cur.execute("Delete from bus where name=? and password=?",(v1.get(),v2.get()))
            conn.commit()
            conn.close()
            Label(new,text="Account deleted Successfully").grid(row=4,column=1)

    Button(new, text="Delete", command=logs, bg='grey', width=10).grid(row=3, column=1, pady=10)

def fun8():
    value=msg.askokcancel("Confirm Exit","Are you sure you want to exit?")
    if(value==1):
        root.quit()

b1=Button(root,text="Create Account",bg='grey',pady=10,command=fun).grid(row=1,column=1,padx=20,pady=10)
b2=Button(root,text="Bus Booking",bg='grey',pady=10,command=fun2).grid(row=1,column=2,padx=20,pady=10)
b3=Button(root,text="Payment",bg='grey',pady=10,command=fun3).grid(row=1,column=3,padx=20,pady=10)
b4=Button(root,text="Bus Cancel",bg='grey',pady=10,command=fun4).grid(row=1,column=4,padx=20,pady=10)
b5=Button(root,text="Your Account",bg='grey',pady=10,command=fun5).grid(row=1,column=5,padx=20,pady=10)
b6=Button(root,text="About",bg='grey',pady=10,width=10,command=fun6).grid(row=1,column=6,padx=20,pady=10)
b7=Button(root,text="Delete Account",bg='grey',pady=10,width=15,command=fun7).grid(row=1,column=7,padx=20,pady=10)
b8=Button(root,text="Exit",bg='grey',pady=10,width=10,command=fun8).grid(row=1,column=8,padx=20,pady=10)

#Extra code for myself for checking how many accounts i have made in this portal
# conn=sqlite3.connect("Data.db")
# cur=conn.cursor()
# cur.execute("Select *from bus")
# data=cur.fetchall()
# conn.commit()
# conn.close()
# for i in data:
#     print(i)

root.mainloop()
