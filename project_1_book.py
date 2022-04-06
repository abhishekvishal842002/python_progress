# # number is even, then collatz() should print number // 2 and return this value.
# # If number is odd, then collatz() should print and return 3 * number + 1.
def collatz(number):
    if number%2==0 :
        a=number//2
        print(a)
        return a
    else:
        b=(3*number)+1
        print(b)
        return b
       
c=input ("a number")
while c!=1:      
    c=int(input("enter an integer"))
    collatz(c)

