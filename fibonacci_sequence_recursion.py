#fibonacci sequence = a sequence in which the first two numbers are 0 1nd 1 
#after that its next term is the sum of previous two numbers
# example :_ 1 2 3 5 8 13 ....n

def fibb(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibb(n-1) + fibb(n-2)

n=int(input("enter an integer:-  "))
i=1
while i<n:
    print(str(fibb(i))+" ",end="")
    i=i+1