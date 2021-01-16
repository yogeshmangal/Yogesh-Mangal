import time
nominee_name1=input("Enter the name of nominee_1 ")
nominee_name2=input("Enter the name of nominee_2 ")

n1_votes=0
n2_votes=0

voter_id=[1,2,3,4,5,6,7,8,9,10]
num_of_votes=len(voter_id)

while True:
    if(voter_id==[]):
        print("\nVoting Session completed")
        print("Counting is in Process...")
        time.sleep(20)
        if(n1_votes>n2_votes):
            percent=(n1_votes/num_of_votes)*100
            print(nominee_name1,"won by",percent,"%votes")
            break
        elif(n2_votes>n1_votes):
            percent=(n2_votes/num_of_votes)*100
            print(nominee_name2,"won by",percent,"%votes")
            break
        else:
            print("Both party got eqaul votes")
            break
        
    else:
        voter=int(input("\nEnter your voter id "))
        if voter in voter_id:
            print("You are a voter ")
            voter_id.remove(voter)
            vote=int(input("Enter your vote 1 or 2 "))
            if(vote==1):
                n1_votes+=1
                print("Thanks for casting vote")
            
            elif(vote==2):
                n2_votes+=1
                print("Thanks for casting vote")
    
        else:
            print("You are not a voter or you have already voted")
        
