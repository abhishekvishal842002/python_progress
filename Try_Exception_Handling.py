x=input("num1  ")
y=input("num2  ")


# print("the sum is " ,(int(x)+int(y)))

# until and unless we give input as a string value the above code will run fine
# but when we give them a string then the code stops and throws an error
# which will make our below statements useless
# but if it is important to execute the below code lines we will use try exception handeling
# as follows:-
try:
    print("the sum is " ,(int(x)+int(y)))
except Exception as e:
    print (e)

#now even if the above print function gets an error then also the below codes will bw executed.


print(x)
print(y)
