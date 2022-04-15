class student:
    no_of_fans=12
    def __init__(self,name,std,section,subjects,fans):
        self.name=name
        self.std=std
        self.section=section
        self.subjects=subjects
        self.fans=fans

    
    def print_details(self):
        return f"the name is {self.name} and the class is {self.std} and the roll is {self.section} and the fans are {self.no_of_fans}"
    
    @classmethod
    def change_fans(cls,newfans):
        cls.no_of_fans=newfans

abhishek= student("abhishek vishal",12,1,0,0)

# print(abhishek.print_details())

abhishek.change_fans(26)

print(student.no_of_fans)