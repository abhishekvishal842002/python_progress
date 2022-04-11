#this program is used for managing the food and exercise record of 3 users
#store each data in 6 different text files.
#with time tag and name of the work done

def getdate():
    import datetime
    return datetime.datetime.now()

name=int(input("TELL ME WHO'S THIS\n"+"Type 1 : if this is HARRY.\n"+"Type 2 : if this is ROHAN.\n"+"Type 3 : if this is HAMMAD.\n"+"TYPE YOUR CHOICE HERE:- "))

if name==1 :
    work=int(input("WHAT ARE YOU DOING.\n"+"Type 1 : for EXERCISE\n"+"Type 2 : for FOOD\n"+"TYPE YOUR CHOICE HERE:- "))    
    if work == 1 :
        with open("HARRY_exercise.txt","a") as f:
            a=input("name of the exercise :-  ")
            f.write(str(getdate())+"  --  "+a+"\n")
    elif work == 2 :
        with open("HARRY_food.txt","a") as f:
            a=input("name of the exercise :-  ")
            f.write(str(getdate())+"  --  "+a+"\n")
    else:
        print("invalid input please try again")
elif name==2 :
    work=int(input("WHAT ARE YOU DOING.\n"+"Type 1 : for EXERCISE\n"+"Type 2 : for FOOD\n"+"TYPE YOUR CHOICE HERE:- "))
    if work == 1 :
        with open("ROHAN_exercise.txt","a") as f:
            a=input("name of the exercise :-  ")
            f.write(str(getdate())+"  --  "+a+"\n")
    elif work == 2 :
        with open("ROHAN_food.txt","a") as f:
            a=input("name of the exercise :-  ")
            f.write(str(getdate())+"  --  "+a+"\n")
    else:
        print("invalid input please try again")
elif name==3 :
    work=int(input("WHAT ARE YOU DOING.\n"+"Type 1 : for EXERCISE\n"+"Type 2 : for FOOD\n"+"TYPE YOUR CHOICE HERE:- "))
    if work == 1 :
        with open("HAMMAD_exercise.txt","a") as f:
            a=input("name of the exercise :-  ")
            f.write(str(getdate())+"  --  "+a+"\n")
    elif work == 2 :
        with open("HAMMAD_food.txt","a") as f:
            a=input("name of the exercise :-  ")
            f.write(str(getdate())+"  --  "+a+"\n")
    else:
        print("invalid input please try again")
else:
    print("invalid input please try again")