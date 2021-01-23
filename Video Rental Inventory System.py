#Video Rental Inventory System

class VideoStore:
    def __init__(self):
        self.listInventory=[]


class Main:
    def __init__(self):
        v=VideoStore()
        while(1):
            print("1.Add Videos:")
            print("2.Check Out Video:")
            print("3.Return Video:")
            print("4.Receive Rating:")
            print("5.List Inventory:")
            print("6.Exit:")
            ch=int(input("Enter your choice (1..6): "))
            if(ch==1):
                M=[None,None,None]
                data=input("Enter the name of video you want to add: ")
                M[0]=data
                v.listInventory.append(M)
                print("Video",data,"added successfully\n")
                
            elif(ch==2):
                data=input("Enter the name of the video you want to check out: ")
                for i in v.listInventory:
                    if(i[0]==data):
                        i[1]=True
                        print("Video",data,"checked out successfully\n")

            elif(ch==3):
                data=input("Enter the name of the video you want to check out: ")
                for i in v.listInventory:
                    if(i[0]==data):
                        i[1]=False
                        print("Video",data,"returned successfully\n")

            elif(ch==4):
                data=input("Enter the name of the video you want to Rate: ")
                for i in v.listInventory:
                    if(i[0]==data):
                        r=int(input("Enter the rating of this video: "))
                        i[2]=r
                        print("Rating",r,"has been mapped to the video",data,"\n")

            elif(ch==5):
                print("\nVideoName  CheckoutStatus Rating")
                for i in v.listInventory:
                    for j in i:
                        print(j,end="        ")
                    print()
                print("\n")

            elif(ch==6):
                print("Exiting..!! Thanks for using the application")
                exit()

            else:
                print("Selected choice is wrong\n")


m=Main()

                
                
                
            


    
