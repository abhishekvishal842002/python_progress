from inspect import ArgSpec


def print_name(n,*a,**q):     #here * denotes args and 
    print(n)                  #     ** denotes quargs
    for i in a:
        print(i)
    for x,y in q.items():
        print(f"the roll of {x} is {y}")



students =5
students_name=["akash","aman","pratyush","raman","anurag"]
students_roll=(1,2,3,4,5)
students_name_roll={"aman":1,"akash":2,"raman":3,"anurag":4,"pratyush":5}
print(type(students_name_roll))
print_name(students,*students_name,*students_roll,**students_name_roll)

#with the use of args and quargs we can add as many 
# lists or tuples in Args 
# dictionaries in quargs