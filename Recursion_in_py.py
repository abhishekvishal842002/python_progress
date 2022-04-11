# recursion means to give the same function in existing function.

def func1(n):
    if n==1:
        return 1
    else:
        return n+func1(n-1)
n=int(input("enter an integer"))
print(func1(n))

#here for rxample if we will take 5 then it will recurse until it reaches 1 i.e.
# 5+func1(4)
#5+4+func1(3)
#5+4+3+func1(2)
#5+4+3+2+func1(1)
#5+4+3+2+1
# 15 is the output.
