from functools import reduce
a=[1,3,5,2,4]
sum=reduce(lambda x,y:x+y,a)
print(sum)