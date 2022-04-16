class student:    #classes
    no_of_fans=12
    def __init__(self,name,std,section,subjects,fans):
        self.name=name      #instances
        self.std=std
        self.section=section
        self.subjects=subjects
        self.fans=fans

    
    def print_details(self):
        return f"the name is {self.name} and the class is {self.std} and the roll is {self.section} and the fans are {self.no_of_fans}"
    
    @classmethod
    def change_fans(cls,newfans):
        cls.no_of_fans=newfans
    
    @classmethod              #as alternative constructor.
    def splitter(cls,string_text):
        string_list=string_text.split("-")
        return cls(string_list[0],string_list[1],string_list[2],string_list[3],string_list[4])


abhishek= student("abhishek vishal",12,1,0,0)     

vishal=student.splitter("vishal kumar-13-14-2-3")      # objects

print(abhishek.print_details())
print(vishal.print_details())