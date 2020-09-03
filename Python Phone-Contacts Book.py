d={}
print("1. Add new Contact")
print("2. Display contacts list")
print("3. Search no.")
print("4. Delete Contact")
print("5. exit")

while(1):
    ch=input("Enter your choice ")
    if(ch=='1'):
        value=input("Enter the contact no ")
        key=input("Enter the name ")
        d[key]=value
    elif(ch=='2'):
        if not bool(d):
            print("Contacts List is empty")
        else:
            print("Name    Contact")
            print()
            for x,y in d.items():
                print(x,":",y)
    elif(ch=='3'):
        key=input("Enter the contact name you want to search ")
        if key in d:
            print(d[key])
        else:
            print("Contact is not found")
    elif(ch=='4'):
        key=input("Enter the contact name you want to delete ")
        if key in d:
            del d[key]
            print("Contact Successfully deleted")
        else:
            print("Contact not found")
    elif(ch=='5'):
        break
    else:
        print("Wrong choice")
