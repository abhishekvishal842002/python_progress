from operator import truediv


row=int(input("give the number of rows:-- "))
a=int(input("choose 0 or 1:-  "))
if a==0:
    for i in range(1,row+1):
        for j in range(i):
            print("* ",end="")
        print("")   
elif a==1:   
    for i in range(row,0,-1):
        for j in range(i):
            print("* ",end="")
        print("")    
else:
    print("invalid input try again!")