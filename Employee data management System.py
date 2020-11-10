class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None
        self.end=None

    def append(self,data):
        temp=Node(data)
        if(self.start==None):
            self.start=self.end=temp
            self.end.next=None
        else:
            self.end.next=temp
            self.end=temp
            self.end.next=None

    def display(self):
        temp=self.start
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()
print("1. Insertion")
print("2. Display")
print("3. Deletion")
print("4. Search any detail by Id no")
print("5. Exit")
M=[]
while(1):
    print()
    ch=int(input("Enter your choice "))
    print()
    if(ch==1):
        n=int(input("Enter the no. of employees "))
        #M=[]
        for i in range(n):
            print()
            print("For",i+1,"employee")
            l=LinkedList()
            l.append(int(input("Enter id ")))
            l.append(input("Enter name "))
            l.append(int(input("Enter Age ")))
            l.append(input("Enter Department Name "))
            l.append(int(input("Enter Salary ")))
            M.append(l)
    elif(ch==2):
        print("Data is: ")
        print("Id   Name  Age  Dept  Salary")
        print("--   ----  ---  ----  ------")
        for i in M:
           i.display()
        print()

#This below code is used to remove particular record from data
    elif(ch==3):
        l1=len(M)
        d=int(input("Enter the id no you want to remove "))
        for i in M:
            if(i.start.data==d):
                M.remove(i)
        N=M
        l2=len(N)
        if(l1==l2):
            print("Sorry,this id is not available")
        print()

    elif(ch==4):
        d=int(input("Enter the id no of employee you want to search "))
        print()
        for i in M:
            if(i.start.data==d):
                print("Id   Name  Age  Dept  Salary")
                print("--   ----  ---  ----  ------")
                i.display()
                break
        else:
            print("Sorry,this id is not avialble")
            print()

    elif(ch==5):
        exit()
    else:
        print("Wrong choice")
        
