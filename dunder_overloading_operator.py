class employee:
    no_of_leaves=8
    def __init__(self,name,salary,role,ctc):
        self.name=name
        self.salary=salary
        self.role=role
        self.ctc=ctc

    def printdetails(self):
        return f"the name is {self.name}. salary is {self.salary} and role is {self.role}"


    
    def __add__(self,other):     #predefined 
        return f"the combined salary is {self.salary+other.salary}.\nthe combined ctc is {self.ctc+other.ctc}."

    def __sub__(self,other):     #predefined 
        return f"the combined salary is {self.salary-other.salary}.\nthe combined ctc is {self.ctc-other.ctc}."

    def __floordiv__(self,other):     #predefined 
        return f"the combined salary is {self.salary/other.salary}.\nthe combined ctc is {self.ctc/other.ctc}."

    def __truediv__(self,other):     #predefined 
        return f"the combined salary is {self.salary//other.salary}.\nthe combined ctc is {self.ctc//other.ctc}."

    def __mul__(self,other):     #predefined 
        return f"the combined salary is {self.salary*other.salary}.\nthe combined ctc is {self.ctc*other.ctc}."

    def __pow__(self,other):     #predefined 
        return f"the combined salary is {(self.salary)**(other.salary)}.\nthe combined ctc is {(self.ctc)**(other.ctc)}."

##########---------------------MORE PREDEF OPERATORS AT---------https://docs.python.org/3.9/library/operator.html---------
#########-----------SELECT HE CURRENT PY LANG FOR BETTER SUPPORT---------------------

emp1=employee("abhishek",100,"programmer",600)
emp2=employee("prashant",25,"sweeper",250)

print(emp1+emp2)
print(emp1-emp2)
print(emp1/emp2)
print(emp1//emp2)
print(emp1*emp2)
print(emp1**emp2)