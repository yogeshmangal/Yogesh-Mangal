#eShopping App

import time
class Shopping:
    def __init__(self):
        self.account={}
        self.isAccount=False
        self.cart={}
        self.total_bill=0
        self.OrderList=[]

    def createAccount(self):
        self.account['Name']=input("\tName: ")
        self.account['Age']=int(input("\tAge: "))
        self.account['Address']=input("\tAddress: ")
        self.account['Mob']=input("\tMobile No: ")
        self.isAccount=True

    def shopping(self):
        d={"Headphones":1500,"Speakers":2100,"TShirt":600,"Pant":1200,"Perfumes":400,"Laptops":45000,"Mobiles":20000}
        print("\n\tAvailable items with their respective prices are:\n")
        for i,j in d.items():
            print("\t",i,":",j)
        i=input("\n\tDo you want to purchase any item(yes/no) ")
        if(i=='yes'):
            print("\n\tEnter the items with space you want to purchase")
            M=list(input("\t").split())
            count=0
            for item in M:
                if item not in d:
                    print("\tCurrently",item,"is not available")
                else:
                    self.cart[item]=d[item]
                    count+=1
            if(count!=0):
                print("\tItems are added to cart")
            else:
                pass
        else:
            pass

    def myAccount(self):
        print("\n\tAccount Details")
        print("\t----------------")
        for i,j in self.account.items():
            print("\t",i,":",j)

    def myOrders(self):
        if(len(self.OrderList)==0):
            print("\tYou have no Orders")
        else:
            print("\tQuantity Item Total Price")
            print("\t-------- ---- -----------")
            for i in self.OrderList:
                print("\t"," ",i[0],"  ",i[1]," ",i[0]*i[2])

    def myCart(self):
        if(len(self.cart)==0):
            print("\tYour cart is empty")
        else:
            print("\n\tItems Available in your cart are:")
            for i,j in self.cart.items():
                print("\t",i,":",j)
            a=input("\n\tDo you want to remove any item from cart(yes/no) ")
            if(a=='yes'):
                print("\tEnter the items with space you want to remove")
                L=list(input("\t").split())
                for i in L:
                    if i in self.cart:
                        self.cart.pop(i)
                        print("\t",i,"removed successfully")
                    else:
                        print("\t",i,"is not in your cart")

            if(len(self.cart)!=0):
                print("\n\tFinal Order")
                for i in self.cart:
                    a=int(input("\tEnter the number of "+i+" "))
                    self.total_bill+=a*self.cart[i]
                    self.OrderList.append((a,i,self.cart[i]))
                print("\tYour total bill is",self.total_bill)
                print("\n\tBilling Methods available are:")
                print("\t1.UPI")
                print("\t2.Debit Card")
                print("\t3.Cash on Delivery")
                ch=int(input("\tEnter your billing choice "))
                if(ch==1 or ch==2):
                    print("\n\tTransaction completed")
                elif(ch==3):
                    print("\n\tYou have to pay",self.total_bill,"at the time of delivery")
                self.cart.clear()
                self.total_bill=0
                print("\tThank you for shopping from YMShopping \U0001F642!!")
                print("\tYour item is Ordered")
                print("\tItem will be delivered within 7 days from now")

s=Shopping()
print("\n\t\t!!!!! \U0001F64F Welcome to YMShopping \U0001F64F !!!!!")
print("\t\t---------------------------------")
q=input("Please type yes to make an account otherwise type no to exit ")
if(q=="yes"):
    print("\n\tAccount Creation")
    print("\t----------------")
    s.createAccount()
    s.isAccount=True
    print("\tCongratulations!! Account created Successfully")
    time.sleep(2)
else:
    print("\nThank You!!")
    exit(0)

if(s.isAccount):
    while(1):
        print("\n1. Shopping")
        print("2. My Cart")
        print("3. My Orders")
        print("4. My Account")
        print("5. Exit")

        ch=int(input("\nEnter your choice "))
        if(ch==1):
            s.shopping()
        elif(ch==2):
            s.myCart()
        elif(ch==3):
            s.myOrders()
        elif(ch==4):
            s.myAccount()
        elif(ch==5):
            print("\nThank You!!")
            exit(0)
        else:
            print("\tWrong choice")
