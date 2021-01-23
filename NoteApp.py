import sqlite3

def addNote():
    conn=sqlite3.connect('data.db')
    cur=conn.cursor()
    cur.execute("create table if not exists notes(title text, note text)")
    title=input("Enter the title of Note ")
    print("Enter your note")
    note=input()
    lst=[title,note]
    cur.execute("insert into notes values(?,?)",lst)
    print("Note Added\n")
    conn.commit()
    conn.close()

def getNotes():
    conn=sqlite3.connect('data.db')
    cur=conn.cursor()
    cur.execute("select *from notes")
    data=cur.fetchall()
    if(data==[]):
        print("No Notes found\n")
    else:
        print()
        for i in data:
            print("Title=>",i[0])
            print("Note=>",i[1])
            print("-------------------------------------------------------")
            print()
    conn.commit()
    conn.close()


def deleteNote():
    conn=sqlite3.connect('data.db')
    cur=conn.cursor()
    title=input("Enter the title of the note you want to delete ")
    cur.execute("delete from notes where title="+str(title))
    print("Note delete successfully\n")
    conn.commit()
    conn.close()



print("1.addNote")
print("2.getNotes")
print("3.deleteNote")
print("4.exit\n")

while(1):
    ch=int(input("Enter your choice "))
    if(ch==1):
        addNote()
    elif(ch==2):
        getNotes()
    elif(ch==3):
        deleteNote()
    elif(ch==4):
        exit()
    else:
        print("wrong choice\n")
