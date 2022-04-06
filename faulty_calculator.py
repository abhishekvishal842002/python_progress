# Faulty Calculator
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result


# solution:--|

o= input("give the operator")
a=int(input("input the following :" " num1= "))
b=int(input("input the following :" " num2= "))
if o=="*" and a==45 or a==3 and a*b==135:
    print("the product is: " + "555")
elif o=="+" and a==56 or a==9 and a+b==65:
    print("the sum is: " + "77")
elif o=="/" and a==56 and b==6:  
    print("the division is: " + "4") 
elif o=="*":
    print("the product is : " + str(a*b))
elif o=="+":
    print("the sum is : " + str(a+b))
elif o=="-":
    print("the subtraction is : " + str(a-b))
elif o=="/":
    print("the division is : " + str(a/b))  
else :
    print("wrong input try again!")