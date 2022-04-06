def func1(a,b):
    '''this is the function for addition'''     #this line is called as a docstring
    print("the sum is ",a+b)

func1(2,3)
print(func1.__doc__)            #this is the way to access any docstring.