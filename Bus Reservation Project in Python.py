import time
print("------Welcome to Mangal Travels------")
print("1.Make Account 2.Bus Booking  3.Payment  4.Bus Cancel  5.About  6.Your Profile 7.Delete Account  8.exit")
d={}; total=0;bus=""
while(1):
    print()
    ch=int(input("Enter your choice "))
    if(ch==1):
        if(len(d)!=0):
            print("\tYou already have account")
        else:
            name=input("\tEnter name ")
            age=int(input("\tEnter your age "))
            mob=int(input("\tEnter mobile no "))
            sex=input("\tEnter your sex(m/f) ")
            city=input("\tEnter your city name ")
            state=input("\tEnter your state name ")
            d['Name']=name
            d['Age']=age
            d['MobNo']=mob
            d['Sex']=sex
            d['City']=city
            d['State']=state

    elif(ch==2):
        if(len(d)==0):
            print("\tYou don't have account. Please first make your account")
        elif(total!=0):
            print("\tYou have already Booked tickets")
        else:
            print()
            print("\tOur Destinations are:\n")
            print("\ta. Dholpur to Agra  : 90Rs/person")
            print("\tb. Dholpur to Delhi : 300Rs/person")
            print("\tc. Dholpur to Murena: 80Rs/person")
            print()
            c=input("\tchoose your destination ")
            if(c=='a'):
                n=int(input("\tEnter the no. of seats you want to reserve "))
                ask=input("\tConfirm booking(yes/no)" )
                if(ask=='yes'):
                    print("\$Recycle.Bint",n,"Tickets confirmed from Dholpur to Agra")
                    bus="Dholpur to Agra"
                    total=total+n*90
                    print("\tTotal fare is",total)
                else:
                    continue
            elif(c=='b'):
                n=int(input("\tEnter the no. of seats you want to reserve "))
                ask=input("\tConfirm booking(yes/no)" )
                if(ask=='yes'):
                    print("\t",n,"Tickets confirmed from Dholpur to Delhi")
                    bus="Dholpur to Delhi"
                    total=total+n*300
                    print("\tTotal fare is",total)
                else:
                    continue
            elif(c=='c'):
                n=int(input("\tEnter the no. of seats you want to reserve "))
                ask=input("\tConfirm booking(yes/no)" )
                if(ask=='yes'):
                    print("\t",n,"Tickets confirmed from Dholpur to Murena")
                    bus="Dholpur to Murena"
                    total=total+n*80
                    print("\tTotal fare is",total)
                else:
                    continue
            else:
                print("\tDestination not found")

    elif(ch==3):
        if(total==0 or len(d)==0):
            print("\tYou don't have any dues..Thank You")
        else:
            print("\tChoose your Payment method:\n")
            print("\ta. Paytm")
            print("\tb. Google Pay")
            print("\tc. PhonePe")
            print("\td. Bhim Upi\n")
            c=input("\tEnter Payment mode ")
            if(c=='a'):
                print("\tMake Payment of",total,"Rs. only on 7728062870")
                time.sleep(10)
                print("\tPayment Received")
                total=0
            elif(c=='b'):
                print("\tMake Payment of",total,"Rs. only on 7728062870")
                time.sleep(10)
                print("\tPayment Received")
                total=0
            elif(c=='c'):
                print("\tMake Payment of",total,"Rs. only on 7728062870")
                time.sleep(10)
                print("\tPayment Received")
                total=0
            else:
                print("\tMake Payment of",total,"Rs. only")
                print("\tUPI-ID: yogeshmangal@upi")
                time.sleep(10)
                print("\tPayment Received")
                total=0

    elif(ch==4):
        if(bus=="" or len(d)==0):
            print("\tYou have not any booking for cancel")
        else:
            c=input("\tDo you confirm cancel booking(yes/no) ")
            if(c=='yes'):
                print("\tTicket Cancelled")
                bus=""
                if(total==0):
                    print("\tYour money will be refunded within 2 or 3 days")
                total=0  
                    
            else:
                continue

    elif(ch==5):
        print("""\n\tIn the hustle and bustle of life, people have no time. They are so busy in their life.
        If they have to travel,they have no time to buy tickets offline . So,there is a need of
        some online tool so that they can easily books their tickets without any difficulties.
        The Bus Reservation Management System provides you this facility. Here, you can reserve
        your sheet and cancel at any time without any risk.""")

    elif(ch==6):
        if(len(d)==0):
            print("\tYou don't have any account")
        else:
            for i,j in d.items():
                print("\t",i," :",j)

    elif(ch==7):
        if(len(d)==0):
            print("\tYou don't have any account")
        else:
            print("\tAccount deleted Successfully")
            d={}

    elif(ch==8):
        print("\n\t---------Thank You!!---------")
        exit(0)

    else:
        print("Wrong choice")
            
            
