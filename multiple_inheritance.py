class electronics:
    def __init__ (self,name,input,output):
        self.name=name
        self.input=input
        self.output=output
    
    def print_det_elect(self):
        print(f"the name of this electronic device is {self.name},\nthe input source is {self.input},\nand the output source is {self.output}")
    
    material="semiconductor"
    
class gadgets:   #here electronics in inherited inside gadgets...
    def __init__(self,use,price):
        self.use=use
        self.price=price
    
    def print_det_gad(self):
        print(f"the use is {self.use}\nand the price is {self.price}")
    
    material="LED"

# multiple inheritance:-
class laptop(electronics,gadgets):         # depends on the order of the arguments.
    def __init__(self,name,input,output,use,price,model,company):
        self.name=name
        self.input=input
        self.output=output
        self.use=use
        self.price=price
        self.model=model
        self.company=company

    def print_det_lap(self):
        print(f"the model is {self.model}\nand the company is {self.company}")

diodes=electronics("diodes","DC","DC")
display=gadgets("as a screen","2000")
macbook=laptop("diodes","DC","DC","as a screen","2000","M1","apple")

macbook.print_det_lap()

print(macbook.material)   #it will get it from the first class because we have given such order to it at line no.=23

