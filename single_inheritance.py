class electronics:
    def __init__ (self,name,input,output):
        self.name=name
        self.input=input
        self.output=output
    
    def print_det_elect(self):
        print(f"the name of this electronic device is {self.name},\nthe input source is {self.input},\nand the output source is {self.output}")
    
    material="semiconductor"
    
class gadgets(electronics):   #here electronics in inherited inside gadgets...
    def __init__(self,name,input,output,use,price):
        self.name=name
        self.input=input
        self.output=output
        self.use=use
        self.price=price
    
    def print_det_gad(self):
        print(f"the name of this electronic device is {self.name},\nthe input source is {self.input},\nthe output source is {self.output},\nthe use is {self.use}\n,and the price is {self.price}")

diodes=electronics("diodes","DC","DC")
display=gadgets("display","AC","image","as a screen","2000")

display.print_det_elect()   #we are acessing the attribute of electronics due to inheritance...
display.print_det_gad()
print(display.material)