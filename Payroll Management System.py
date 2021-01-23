##Given the following table containing information about employees of an organization, develop a
##small python application, which accepts employee id from the command prompt and displays the
##following details as output:
##EmpNo EmpName Department Designation Salary
##In your program, you must initialize an array with the following details.

details=[['Emp_No','Emp_Name','Join_Date','Designation_Code','Department','Basic','HRA','IT'],
         [1001,'Ashish','01/04/2019','e','R&D',20000,8000,3000],
         [1002,'Sushma','23/08/2012','c','PM',30000,12000,9000],
         [1003,'Rahul','12/11/2008','k','Acct',10000,8000,1000],
         [1004,'Chahat','29/01/2013','r','Front Desk',12000,6000,2000],
         [1005,'Ranjan','16/07/2005','m','Engg',50000,20000,20000],
         [1006,'Suman','01/01/2000','e','Manufacturing',23000,9000,4400],
         [1007,'Tanmay','12/06/2006','c ','PM',29000,12000,10000]]


designation=[['Designation_code','Designation','DA'],
             ['e','Engineer',20000],
             ['c','Consultant',32000],
             ['k','Clerk',12000],
             ['r','Receptionist',15000],
             ['m','Manager',40000]]


##Note 1: Salary should be calculated as (Basic + HRA + DA – IT)
##Expected Output format: 
## If you execute the command  1003, the output should be –
##Emp No. Emp Name Department Designation Salary
##1003 Rahul Acct Clerk 29000
## If you execute the command 123, the output should be –
##There is no employee with empid : 123

n=int(input("Enter the Employee id "))
M=[]
flag=False
for i in details:
    if(i[0]==n):
        flag=True
        M.append(i[0])
        M.append(i[1])
        M.append(i[4])
        salary=i[5]+i[6]-i[7]
        dc=i[3]
        for j in designation:
            if(j[0]==dc):
                M.append(j[1])
                salary+=j[2]
                M.append(salary)
        break
        
if(flag==True):
    print("\nEmpNo. EmpName Department Designation Salary")
    for i in M:
        print(i,end="     ")
else:
    print("There is no employee with empid:",n)
        
        
         
