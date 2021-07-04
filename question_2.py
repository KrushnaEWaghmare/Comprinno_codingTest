#1.	Take number of test as input T.
#2.	Perform all validity check on T (1 ≤ T ≤ 1000)
#3.	Create a blank list
#4.	Append values of a,b.c
#5.	Assign the index values to a,b,c
#6.	Check the condition a[0]<=b[0]<=c[0] and a[1]<=b[1]<=c[1] and a[2]<=b[2]<=c[2]:if true then return yes else return no
#7.	Store the splited  each element I in ans[]

def solve(a,b,c):
    if a == b or a == c or b == c:      
        return('no')
    d=[]                                #creates list and append the values of a,b,c
    d.append(a)
    d.append(b)
    d.append(c)
    d.sort()                           #sort the list
    a,b,c=d[0],d[1],d[2]
    if a[0]<=b[0]<=c[0] and a[1]<=b[1]<=c[1] and a[2]<=b[2]<=c[2]:
        return('yes')
    return('no')
    

ans=[]
for i in range(int(input())):
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    c=list(map(int, input().split()))
    ans.append(solve(a,b,c))

for i in ans:
    print(i)
