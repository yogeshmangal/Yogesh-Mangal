#Project: Vaccine Registeration System GUI

from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as msg
import sqlite3

root=Tk()
root.title("Vaccine Registeration System")
root.geometry("1700x1045")
f1=Frame(root,bg='black',borderwidth=8,relief=SUNKEN)
f1.pack(anchor='s',fill=X)
Label(f1,text="!! Stay Safe, Stay Healthy, Stay Vaccinated !!",bg='green',fg='white',font="Helvetica 18 bold",pady=10).pack(fill=X)

photo=ImageTk.PhotoImage(Image.open('vaccine.jpeg'))
Label(image=photo).pack()

f2=Frame(root,bg='orange',borderwidth=10,relief=RIDGE)
f2.pack(fill=X,pady=20)

def registeration():
    top=Toplevel()
    top.title("Registeration Portal")
    top.geometry("644x345")
    Label(top,text="Fill the Details below for Registeration",font="Arial 18 bold",pady=10).grid(row=0,column=1)
    name=Label(top,text="Name",padx=10,pady=5).grid(row=1,column=0,padx=30)
    age=Label(top,text="Age",padx=10,pady=5).grid(row=2,column=0)
    gender=Label(top,text="Gender",padx=10,pady=5).grid(row=3,column=0)
    adhaar=Label(top,text="Aadhar No",padx=10,pady=5).grid(row=4,column=0)
    phone=Label(top,text="Mobile",padx=10,pady=5).grid(row=5,column=0)

    e1=Entry(top,width=25)
    e1.grid(row=1,column=1)
    e2=Entry(top,width=25)
    e2.grid(row=2,column=1)
    var=StringVar()
    var.set("None")
    e3=OptionMenu(top,var,"Male","Female","Other")
    e3.grid(row=3,column=1)
    e4=Entry(top,width=25)
    e4.grid(row=4,column=1)
    e5=Entry(top,width=25)
    e5.grid(row=5,column=1)

    def submit():
        conn=sqlite3.connect('Vaccine_data.db')
        cur=conn.cursor()
        cur.execute("""create table if not exists vaccine(
                        name text, age integer, gender text, adhaar text, phone text)""")
        if(e1.get()=="" or e2.get()=="" or var.get()=="None" or e4.get()=="" or e5.get()==""):
            Label(top, text="Please fill all the fields", font="Arial 10").grid(row=7, column=1)
        else:
            cur.execute("insert into vaccine values(:A,:B,:C,:D,:E)",
                        {'A':e1.get(),
                         'B':e2.get(),
                         'C':var.get(),
                         'D':e4.get(),
                         'E':e5.get()})
            # cur.execute("select oid,*from vaccine")
            # data=cur.fetchall()
            # print(data)
            conn.commit()
            conn.close()
            Label(top,text="Registeration Successfull",font="Arial 10").grid(row=7,column=1)
            Label(top,text="You will get message regarding vaccination on the registered mobile no.",font="Arial 10").grid(row=8,column=1)
            e1.delete(0,END)
            e2.delete(0,END)
            var.set("None")
            e4.delete(0,END)
            e5.delete(0,END)

    def destroy2():
        ans = msg.askyesno("Confirm Exit", "Are you sure you want to exit?")
        if (ans == True):
            top.destroy()

    Button(top,text="Submit",bg='grey',padx=10,command=submit).grid(row=6,column=1,pady=10)
    Button(top,text="Exit",bg='grey',padx=10,command=destroy2).grid(row=6,column=2,pady=10)

def vaccinated_people_details():
    top=Toplevel()
    top.geometry("644x345")
    top.title("Vaccinated People Details")
    Label(top,text="Vaccinated People Details",font="Arial 18 bold underline",pady=10).pack()
    try:
        conn=sqlite3.connect('Vaccine_data.db')
        cur=conn.cursor()
        cur.execute("Select oid,* from vaccine")
        data=cur.fetchall()
        Label(top,text="SNo      Name      Age      Gender      Aadhar      Phone",font="Arial 12 bold").pack()
        Label(top,text="------------------------------------------------------------------------------------------",font="Arial 10 bold").pack()
        for i in data:
            x=""
            for j in i:
                x+=str(j)+"   "
            Label(top,text=x,font="Arial 12").pack()
        conn.commit()
        conn.close()
    except:
        Label(top,text="!! No people have vaccinated till now !!",font="Arial 14",fg="Red").pack()

    Button(top, text="Exit", bg='grey', padx=10, command=top.destroy).pack(pady=40)

def vaccine_details():
    top=Toplevel()
    top.geometry("1700x1045")
    top.title("Vaccine Details")
    f4=Frame(top,borderwidth=8,relief=RIDGE)
    f4.pack(fill=X)
    Label(f4,text="Basic details",font="Aial 14 bold",fg='white',bg='black',pady=10).pack(fill=X)
    txt="""India began administration of COVID-19 vaccines on 16 January 2021. As of 10 May 2021,India has administered 170,153,432 doses overall,
    including first and second doses of the currently-approved vaccines. Two vaccines received approval for emergency use in India at the 
    onset of the programme, including Covishield (a version of the Oxford–AstraZeneca vaccine manufactured by the Serum Institute of India),
    and Covaxin (developed by Bharat Biotech). In April 2021, Sputnik V was approved as a third vaccine, with deployment expected to begin by
    late May 2021."""
    Label(f4,text=txt,font="Arial 12 bold",pady=30,bg='green',fg='white').pack(fill=X)
    Label(f4, text="Types of Vaccine", font="Aial 14 bold", fg='white', bg='black', pady=10).pack(fill=X)
    Label(f4,text="1. Covishield",font="Helvetica 18 bold").pack()
    txt="""The Oxford-AstraZeneca vaccine is being manufactured locally by the Serum Institute of India, the world's largest vaccine manufacturer. 
    It says it is producing more than 60 million doses a month.The vaccine is made from a weakened version of a common cold virus (known as an 
    adenovirus) from chimpanzees. It has been modified to look more like coronavirus - although it can't cause illness. When the vaccine is injected 
    into a patient, it prompts the immune system to start making antibodies and primes it to attack any coronavirus infection. The jab is administered 
    in two doses given between four and 12 weeks apart. It can be safely stored at temperatures of 2C to 8C and can easily be delivered in existing 
    health care settings such as doctors' surgeries."""
    Label(f4,text=txt,font="Arial 12 bold",pady=30,bg='green',fg='white').pack(fill=X)
    Label(f4, text="2. Covaxine", font="Helvetica 18 bold").pack()
    txt="""Covaxin is an inactivated vaccine which means that it is made up of killed coronaviruses, making it safe to be injected into the body. 
    Bharat Biotech, a 24-year-old vaccine maker with a portfolio of 16 vaccines and exports to 123 countries, used a sample of the coronavirus, 
    isolated by India's National Institute of Virology. When administered, immune cells can still recognise the dead virus, prompting the immune 
    system to make antibodies against the pandemic virus."""
    Label(f4, text=txt, font="Arial 12 bold", pady=30, bg='green', fg='white').pack(fill=X)

def about():
    top=Toplevel()
    top.geometry("1700x1045")
    top.title("About")
    f5=Frame(top,borderwidth=5,relief=SUNKEN)
    f5.pack(fill=X)
    Label(f5,text="FACT",font="Arial 20 bold",bg='green',fg='white').pack(fill=X)
    txt="YOU SHOULD STILL WEAR MASK EVEN AFTER RECEIVING YOUR VACCINE"
    Label(f5,text=txt,font="Arial 14",bg='green',fg='white').pack(fill=X)
    txt="""We don't yet know whether getting a COVID-19 vaccination will prevent you
    from spreading the virus to other people, even if you don't get sick yourself. Until
    we know more, we should continue using all the tools available to help stop this pandemic."""
    Label(f5,text=txt,font="Helvetica 12 bold",pady=20,bg="powder blue").pack(fill=X)
    txt="Vaccination gives us hope that the pandemic will end"
    Label(f5,text=txt,font="Helvetica 20 bold",bg='orange',fg='white').pack(fill=X)
    txt="""But in the meantime, we need to continue safety measures to keep the virus from spreading:
    \n>> Wear a mask\n\n>> Physically distance from others\n\n>> Wash your hands\n\n>> Avoid gatherings
    \n>> Stay home when you're sick"""
    Label(f5,text=txt,font="Helvetica 12 bold",pady=20,bg='powder blue').pack(fill=X)
    Label(f5, text="""PLEASE BE SAFE AND KEEP VACCINATED
    \n!!! JAI HIND !!!""", font="Arial 24 bold", bg='brown', fg='white',pady=20).pack(fill=X)


def destroy():
    ans=msg.askyesno("Confirm Exit","Are you sure you want to exit?")
    if(ans==True):
        root.destroy()

b1=Button(f2,text="Register for Vaccination",font="Arial 10 bold",padx=5,pady=10,bg='pink',fg='black',command=registeration)
b1.pack(side=LEFT,padx=40,pady=60)
b2=Button(f2,text="Vaccinated people details",font="Arial 10 bold",padx=5,pady=10,bg='pink',fg='black',command=vaccinated_people_details)
b2.pack(side=LEFT,padx=40,pady=60)
b3=Button(f2,text="Vaccine name and details",font="Arial 10 bold",padx=5,pady=10,bg='pink',fg='black',command=vaccine_details)
b3.pack(side=LEFT,padx=40,pady=60)
b4=Button(f2,text="About",font="Arial 10 bold",padx=10,pady=10,width=15,bg='pink',fg='black',command=about)
b4.pack(side=LEFT,padx=40,pady=60)
b5=Button(f2,text="Exit",font="Arial 10 bold",padx=10,pady=10,width=10,bg='pink',fg='black',command=destroy)
b5.pack(padx=40,pady=60)

f3=Frame(root,bg='grey',borderwidth=8,relief=SUNKEN)
f3.pack(fill=X)

Label(f3,text="Hello Everyone, this portal is created by Yogesh Mangal and Please be Safe and Keep Vaccinated. !!Thank You!!",bg='black',fg="white",font="Arial 10 bold",pady=20).pack(pady=28,fill=X)


mainloop()
