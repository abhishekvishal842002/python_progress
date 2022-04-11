#WITHOUT USING LAMBDA FUNCTION.....

# def a_first(a):
#     return a[1]

# a=[[1,14],[5,6],[8,23]]
# a.sort(key=a_first)
# print(a)



#WITH THE USE OF LAMBDA FUNCTION
a=[[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)
