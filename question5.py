try:
    for _ in range(int(input())):                     #accept input
        n = int(input())
        l = list(map(int, input().split()))           #split the input 
        cnt = [l.count(-1), l.count(0), l.count(1)]
        c = len(l) - sum(cnt)
        
        if c > 1:
            print("no")
        else:

            if c and cnt[0]:
                print("no")
            elif (cnt[0]>1 and cnt[2] == 0) :
                print("no")
            else:
                print("yes")
except:
    pass
