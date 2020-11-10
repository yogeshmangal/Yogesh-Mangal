#Food ordering Management System

import time
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
            print(temp.data,end='  ')
            temp=temp.next
        print()

def food():
    M=[]
    l1=LinkedList()
    l2=LinkedList()
    l3=LinkedList()
    l4=LinkedList()
    l5=LinkedList()
    l6=LinkedList()
    l7=LinkedList()
    l8=LinkedList()
    l9=LinkedList()

    l1.append(5)
    l1.append("Burger")
    l1.append(120.23)
    l1.append(23)
    M.append(l1)

    l2.append(6)
    l2.append("Pizza")
    l2.append(100.67)
    l2.append(13)
    M.append(l2)

    l3.append(1)
    l3.append("Hot Cake")
    l3.append(720.83)
    l3.append(8)
    M.append(l3)

    l4.append(2)
    l4.append("Coffee")
    l4.append(70.23)
    l4.append(46)
    M.append(l4)

    l5.append(3)
    l5.append("Ice-Cream")
    l5.append(70.23)
    l5.append(46)
    M.append(l5)

    l1.display()
    l2.display()
    l3.display()
    l4.display()
    l5.display()
    print()
    n=int(input("Enter the food no to place your order "))
    for i in M:
        if(i.start.data==n):
            print("Selected item is",i.start.next.data)
            print("Its price is",i.start.next.next.data)
            k=int(input("Enter the no. of items "))
            if(k>i.end.data):
                print("Sorry Sir/Madam, this item is out of Stock")
            else:
                print("Order Successfully placed")
                total_bill=k*i.start.next.next.data
                print("Total bill is",total_bill)
    global l
    l=total_bill

def payment():
    print("1. Cash")
    print("2. Paytm/Google-pay")
    print("3. BHIM-UPI")
    print()

    '''if(l==0):
        print("You have already pay the bill or your total bill is Null")
        print()'''
    c= int(input("Choose your payment method "))
    if(c==1):
        print("Pay",l,"Rs. only")
        time.sleep(10)
        print("Payment Received")
    elif(c==2):
        print("Make payment of ",l,"Rs.on this below no.")
        print("Paytm No: 7728062870")
        time.sleep(10)
        print("Payment Received Successfully")
    elif(c==3):
        print("Pay Rs.",l,"on thi below UPI Id")
        print("UPI-ID: yogeshmangal@upi")
        time.sleep(10)
        print("Payment Received")
    else:
        print("Wrong payment method")    
            

print("Welcome to our Food Court".center(60,"!"))
print()
print("1. Food List and order")
print("2. Pay the bill ")
print("3. Exit")

while(1):
    print()
    ch=int(input("Enter your choice "))
    if(ch==1):
        print()
        print("No  Name  Price  InStock")
        print("--  ----  -----  -------")
        food()

    elif(ch==2):
          payment()    

    elif(ch==3):
        print("Thanks for Ordering Food")
        quit()

    else:
        print("Wrong choice selected")
    
