#1.number of test cases
#2.split and apply int to to every element
#3.starting turn valute is 0 and every increment the value increments and and multiple the value of 2 times of number
#4.(a = 2, b = 2) in first turn and max(a, b)/min(a, b) = 2/2 print ans that is 1.


d = int(input())                              #input accept
for i in range(d):
    t = [int(i) for i in input().split()]     #applies int to each string element in the input
    a, b, n = t[0], t[1], t[2]                 #assign the values to a,b,n
    na, nb = 0, 0                               #multiple the value of a and b as respective to the change in value n
    if n % 2 == 1:
        a = a*2
    print(max(a,b)//min(a,b))
