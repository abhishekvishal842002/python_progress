# ask user to give a number n.
#1. take a random number from 1-n.
#2. The number of guesses should be limited,and set according to the range taken by user).
# for n number of range the no. of attempts should be n//3
#3. Print the number of guesses left.
#4. Print the number of guesses he took to win the game.
#5. The “Game Over” message should display if the number of guesses becomes equal to 0.

import random
print("welcome to the game!\n","all the best!")
a=int(input("tell us the number (integer) upto which you want to play:- "))
b=a//3
print("you have "+str(b)+" attempts.")
r_num=random.randint(1,a)
num=int(input("lets start\ninput an integer between 1 to 20:-  "))
count=1
while num!=r_num :
    if count==b:
        print("your attempts are over!😭😭😭 \n","game over")
        print("This game was created by ABHISHEK VISHAL")
        break
    elif num<r_num and num >0:
        print("think of a bigger number")
        print("you are left with "+str(b-count)+" attempts")
        count+=1
    elif num>r_num and num<a:
        print("think of a smaller number")
        print("you are left with "+str(b-count)+" attempts")
        count+=1
    else:
        print("invalid output! please write a integer between 1 to 20") 
        print("you are left with "+str(b-count)+" attempts")
        count+=1
    num=int(input("input an integer between 1 to 20:-  "))
if num==r_num:
        print("congratulations!🥳🥳🎊🎉🍾🍾🥂🙌\n","you have finished the game in "+str(count)+" attempts.\n"+"This game was created by ABHISHEK VISHAL")