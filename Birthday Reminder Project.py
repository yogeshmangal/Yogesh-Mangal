#Birthday Reminder Project

class Birthday:
    def __init__(self):
        self.d={}

    def show(self):
        if len(self.d)==0:
            print("Nothing to show")
        else:
            name=input("Enter name to person you want to look for birthday ")
            if name in self.d:
                print("Birthday is on",self.d[name])
            else:
                print("No data found")

    def add(self,name,date):
        if name in self.d:
            print("This name already exists")
        else:
            self.d[name]=date
            print("Birthday Added")


b=Birthday()
print("-----------Birthday App--------------")
print("\n1.Show Birthday")
print("2.Add to Birthday List")
print("3.Exit")
while(1):
    ch=int(input("Enter your choice "))
    if(ch==1):
        b.show()
    elif(ch==2):
        name=input("Enter friend's name ")
        date=input("Enter Birthday date ")
        b.add(name,date)
    elif(ch==3):
        exit()
    else:
        print("Wrong choice")
