T = int(input())                            #accept input
for x in range(T):
    N=int(input())
    L=list(map(int,input().split()))        #applies int to each string element in the input
    L1=[]                                   #blank list
    for x in L:
        if L.count(x)>=2:                   #check condition in count of x greater than and equal to 2 then append the x in L1.
            L1.append(x)
    L1.sort(reverse=True)                   #sort the L1
    if len(L1)>3:                           #length of L1 is greater than 3 then then print the rectangke area
        print(L1[0]*L1[3])
    else:
        print("-1")
