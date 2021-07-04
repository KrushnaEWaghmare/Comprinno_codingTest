#algorith or pseudo code
#1.	Take number of test as input T.
#2. applies int to each string element in the input
#3.check the salary if greater than 1500 .
#4.if salary is greater than then calculate the gross calculate will be HRA is 10% if salary and DA is 90% basic salary
#5.print the gross salary




T=int(input())                          #accept the test cases
for i in range(T):                      
    s=int(input())                       #int input
    if(s<1500):                           #if salary is greater than 1500 then calculate the gross salary s+0.1*s+0.9*s else s+500+0.98*s 
        g=s+0.1*s+0.9*s 
    else:
        g=s+500+0.98*s 
    print(g)
