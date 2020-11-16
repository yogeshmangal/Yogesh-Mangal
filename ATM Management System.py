# ATM Management System
#Run this code on cmd not on IDLE
from getpass import getpass
import time

class ATM:
    def __init__(self,name,AcNo,bal,pin):
        self.name=name
        self.AcNo=AcNo
        self.bal=bal
        self.pin=pin
        self.cur=0

    def withdraw(self):
        while(1):
            p=getpass("\tEnter the pin ")
            if(int(p)==self.pin):
                break
            else:
                print("\tEnter the correct pin")
        amt=int(input("\tEnter the amount to withdraw "))
        if(self.bal-amt<0):
            print("\tYou have not enough balance to withdraw ")
        else:
            self.cur=amt
            self.bal=self.bal-amt
            print("\tProcessing...")
            time.sleep(10)
            print("\tAmount successfully withdawn")
            c=input("\tDo you want to print receipt(yes/no) ")
            if(c=='yes'):
                print("\n\t  Punjab National Bank")
                print("\t---------------------------")
                print("\tName of A/c Holder:",self.name)
                print("\tAccount No is:",self.AcNo)
                print("\tcurrently withdrawn amount is:",self.cur)
                print("\tRemaining balance is:",self.bal)
                

    def change_pin(self):
        p=getpass("\tEnter the current pin ")
        if(int(p)!=self.pin):
            print("\tcurrent pin is wrong")
        else:
            np=getpass("\tEnter the new pin ")
            if(len(str(np))!=4):
                print("\tLength of pin should be 4")
            else:
                self.pin=int(np)

    def check_cur_bal(self):
        print("\tYour current balance is",self.bal)


print("1.Withdraw Balance   2.Change your Pin   3.Check Balance   4.exit")
a=ATM('Yogesh Mangal',9079681713,20000,8875)
while(1):
    ch=int(input("\nEnter your choice "))
    if(ch==1):
        a.withdraw()
    elif(ch==2):
        a.change_pin()
    elif(ch==3):
        a.check_cur_bal()
    elif(ch==4):
        exit()
    else:
        print("wrong choice")
