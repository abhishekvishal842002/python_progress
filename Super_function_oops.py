from typing import ClassVar


class x:
    classvar1="this is going good."
    def __init__(self):
        self.var1="i am inside A's constructor"
        self.classvar1="instance var inside class A."
        self.special="special"

class y(x):
    classvar1="i'm in class B."
    def __init__(self):
        super().__init__()
        self.var1="i'm inside B's constructor."
        self.classvar1="instance var in class B."

a=x()
b=y()

print (b.classvar1)
print(b.special)