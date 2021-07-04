#1.Accept the input
#2.Apply int to each string element in the input\
#3.store the input in list
#4.sort the list by using inbuild sort()
#5.print the min value by using the min() and decrement the array size by 1

for i in range(int(input())):                     #accept inputs
    ele=int(input())                               #store it in ele
    l=map(int,input().split())                    
    l=list(l)                                     #convert to list
    l.sort()                                       #sort the list by using sort function
    print(min(l)*(ele-1))                           #print minimun and decrease the array size y -1
