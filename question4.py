#1.	Take number of test as input T.
#2.	Perform all validity check on T (1 ≤ T ≤ 50 1 ≤ N ≤ 50)
#3.	Split the input by using split()
#4.	Set a variable c=0 which check the count
#5.	Check condition for cookie if yes then increment the count of c by 1 else set it as 0
#6.	Check the count of cookie is equal to 2 then break the loop by using Break
#7.	And last check value of c==0 then print Yes otherwise print No





t=int(input())            #take input t
for k in range(t):        
    n = int(input())      #stores the input in n.
    l = input().split()   #split a string and return a list of words and store in l .
    c=0
    for i in l:             
        if i=="cookie":   #check codition if i equal to cookies
            c+=1          #increment the count of c   
        else:              
            c=0           #else set c value to 0
            
        if c==2:          
            break
    if c==0:
        print("YES")
    else: 
        print("NO")
