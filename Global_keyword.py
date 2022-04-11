
a=10
def func1():
    global a  #here global keyword is used for
                # changing and manipulating the 
                # value of a global variable in
                #  local space
    a=a+5
    print(a)
func1()