#Algorithm or Pseudo 
#take the input case
#apply the if conditions for "B" or "b" then print "Battleship"
#if input is "C" or "c" then print Cruiser
#if input is "D" or "d" then print Destroyer
#if input is "F" or "f" then print Frigate

   n=int(input())
for i in range(n):                            #input
    num=input()
    if(num=='B' or num=='b'):                 #if condition for Num="B" or "b"
        print("BattleShip")
    elif(num=='C' or num=='c'):               #if condition for Num="C" or "c"
        print("Cruiser")
    elif(num=='D' or num=='d'):               #if condition for Num="D" or "d"
        print("Destroyer")
    elif(num=='F' or num=='f'):                #if condition for Num="F" or "f"
        print("Frigate")
