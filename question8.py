d = int(input())                              #input accept
for i in range(d):
    t = [int(i) for i in input().split()]     #applies int to each string element in the input
    a, b, n = t[0], t[1], t[2]                 #assign the values to a,b,n
    na, nb = 0, 0                               #multiple the value of a and b as respective to the change in value n
    if n % 2 == 1:
        a = a*2
    print(max(a,b)//min(a,b))
