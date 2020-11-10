q1="""Q1.Is Python case sensitive when dealing with Identifiers?
a. Yes
b. No
c. Machine Dependent
d. None"""

q2="""Q2.Which of the following is not a keyword?
a. eval
b. assert
c. local
d. pass"""

q3="""Q3.Which one of these is floor division?
a. /
b. //
c. %
d. None"""

q4="""Q4.What is the output of this 3*1**3?
a. 27
b. 9
c. 3
d. 1"""

q5=""""Q5.a"+"bc"=?
a. a
b. bc
c. bca
d. abc"""

import time
d={q1:"a",q2:"a",q3:"b",q4:"c",q5:"d"}

name=input("Enter your name: ")
print("hello",name,"welcome to the quiz")
print("Your quiz will appear within 10 Seconds ")
time.sleep(10)
score=0
for i in d:
    print()
    print(i)
    skip=input("Do you want to skip the question(yes/no) ")
    if(skip=='yes'):
        continue
    ans=input("enter answer(a/b/c/d): ")
    if(ans==d[i]):
        print("correct answer and you got 1 point")
        score+=1
    else:
        print("wrong answer and you lost 1 point")
        score-=1

    out=input("Do you want to quit the quiz(yes/no) ")
    if(out=='yes'):
        break

print()
print("Final score is",score)
        
    
    
