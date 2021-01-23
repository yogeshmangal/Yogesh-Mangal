#e-Payment App

import random
class YPay:
    def __init__(self):
        self.name=None
        self.no=None
        self.age=None
        self.KYC=None
        self.wallet_balance=None
        self.bankAccount=None

    def createAccount(self):
        print("\n*******Account Creation*******\n")
        self.name=input("Enter your name ")
        self.no=input("Enter you Mobile No. ")
        self.age=int(input("Enter your age "))
        if(self.age>18):
            self.KYC=True
        else:
            self.KYC=False
        self.wallet_balance=100
        print("Congratulations!!You get 100 Rs. Cashback for creating account\n")

    def yourAccountDetails(self):
        print("\n*******Your Account Details*******\n")
        print("Name")
        print(self.name)
        print("-----------------")
        print("Mob. No.")
        print(self.no)
        print("-----------------")
        print("Age")
        print(self.age)
        print("-----------------")
        if(self.KYC==True):
            print("KYC Verfified\n")
        else:
            print("KYC not Verified\n")

    def addBankAccount(self):
        print("Enter the name of the bank you want to link")
        bankAccount=input()
        print("Enter your linked mobile no.")
        no=input()
        if(self.no==no):
            print("Mobile No. verified")
            print("Bank Added Successfully\n")
            self.bankAccount=bankAccount
        else:
            print("Mobile no. is not linked with this bank\n")

    def addBalancetoWallet(self):
        amount=int(input("Enter the amount to you wanna add "))
        if(amount>5000 and self.KYC==False):
            print("Sorry!! you don't have KYC so you can't add more than 5000 Rs.\n")
        else:
            no=input("Enter you mob. to verify ")
            if(no==self.no):
                print("Verfication done")
                self.wallet_balance+=amount
                print("Amount added Successfully from",self.bankAccount,"\n")
            else:
                print("Sorry!! Mobile not not verified\n")


    def pay_by_wallet(self):
        no=int(input("Enter the Mob. no you want to pay "))
        amount=int(input("Enter the amount you want to pay "))
        if(amount>self.wallet_balance):
            print("Your wallet don't have enough money. Please recharge the wallet\n")
        elif(amount<=0):
            print("Please enter valid amount\n")
        else:
            self.wallet_balance-=amount
            print("Payment done succesfully\n")
            p=random.randint(1,5)
            if(p==2):
                print("Hurray!! you got a cashback of 10Rs\n")
                self.wallet_balance+=10
                

    def get_wallet_balance(self):
        return self.wallet_balance


p=YPay()
print("1. Create Account")
print("2. Your Account")
print("3. Add Bank Accounts")
print("4. Add money to Wallet")
print("5. Pay by Wallet")
print("6. Check Wallet Balance")
print("7. Exit\n")

while(1):
    ch=int(input("Enter your choice "))
    if(ch==1):
        if(p.name==None):
            p.createAccount()
        else:
            print("Your account have already registerd on",p.name,"\n")

    elif(ch==2):
        if(p.name==None):
            print("You don't have any account\n")
        else:
            p.yourAccountDetails()

    elif(ch==3):
        if(p.name==None):
            print("You don't have any Account\n")
        elif(p.bankAccount!=None):
            print("You have alreay added",p.bankAccount,"to your Account\n")
        else:
            p.addBankAccount()

    elif(ch==4):
        if(p.name==None):
            print("You don't have any account\n")
        elif(p.bankAccount==None):
            print("You don't have any bank account to add money\n")
        else:
            p.addBalancetoWallet()

    elif(ch==5):
        if(p.name==None):
            print("You don't have any account\n")
        elif(p.wallet_balance==None or p.wallet_balance==0):
            print("Payment Failed!!")
            print("Your wallet is empty\n")
        else:
            p.pay_by_wallet()

    elif(ch==6):
        if(p.name==None):
            print("You don't have any account\n")
        elif(p.wallet_balance==None or p.wallet_balance==0):
            print("0\n")
        else:
            print(p.get_wallet_balance(),"Rs.\n")

    elif(ch==7):
        print("Thank you!! for using Ypay App\n")
        exit()

    else:
        print("Wrong choice\n")
