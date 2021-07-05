
T=int(input())                                  #input tests
for i in range(T):                              
    c,d,l=map(int,input().split())
    if l%4==0:                                  #condition for 4 legs
        if l<=4*(c+d) and l>=4*max(c-d,d):      #it check condition for leg 4 and leg 8
            print('yes')                        #print yes if condition satisfied
        else:
            print('no')                         #else print no
    else:
        print('no')
