for i in range(int(input())):                     #accept inputs
    ele=int(input())                               #store it in ele
    l=map(int,input().split())                    
    l=list(l)                                     #convert to list
    l.sort()                                       #sort the list by using sort function
    print(min(l)*(ele-1))                           #print minimun and decrease the array size y -1
