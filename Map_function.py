#USECASE 1

# num=["1","2","3","4"]
# print(f'before{num}')
# a=list(map(int,num))
# print(f'after{a}')




# USECASE 2

# num=[1,2,3,4]
# square=list(map(lambda x:x*x,num))
# print(square)




#USECASE 3 (advanced usecase)


List1=[1,4,2,5]

def square(a):
    return a*a 

def cube(a):
    return a*a*a 

List2=[square,cube]
for i in List1:
    a=list(map(lambda x:x(i),List2))
    print(a)