class student:
    no_of_fans=12
    
    def print_details(self):
        return f"the name is {self.name} and the class is {self.std} and the roll is {self.section} and the fans are {self.no_of_fans}"

abhishek= student()
vishal=student()

abhishek.name="abhishek vishal"
abhishek.std=12
abhishek.section=1

vishal.name="vishal kumar"
vishal.std=11
vishal.section=3
vishal.subjects=["physics","chemistry","biology"]

# print(student.no_of_fans)

print(vishal.print_details())