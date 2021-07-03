from collections import Counter  #counter is a sub-class available inside the dictionary class
for i in range(int(input())): #take input
    n= input() #store the input in n.
    c = []
    d = dict(Counter(n))   #dictionay
    for e in d.values():  #checks the dict values
        c.append(e)       #append those values in list
    c.sort()              #sort the list by using sort() function
    if len(c)<3:          #checks the condition if length of sorted list is greated than 3 then print dynamic else perform else part
        print("Dynamic")
    else:
        if c[-1] != c[-2]+c[-3]:    #checks the condition that f(ci)=f(ci-1)+f(ci-2)
            print("Not")
        else:
            print("Dynamic")
