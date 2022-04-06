#1. take a random number from 1-20.
#2. The number of guesses should be limited, i.e (5 or 9).
#3. Print the number of guesses left.
#4. Print the number of guesses he took to win the game.
#5. The “Game Over” message should display if the number of guesses becomes equal to 0.

import random
r_num=random.randint(1,20)
print("welcome to the game!\n","you have got 9 attempts to guess the auto generated number\n","all the best!")
num=int(input("input an integer between 1 to 20:-  "))
count=1
while num!=r_num :
    if count==9:
        print("your attempts are over!😭😭😭 \n","game over")
        print("This game was created by ABHISHEK VISHAL")
        break
    elif num<r_num and num >0:
        print("think of a bigger number")
        print("you are left with "+str(9-count)+" attempts")
        count+=1
    elif num>r_num and num<20:
        print("think of a smaller number")
        print("you are left with "+str(9-count)+" attempts")
        count+=1
    else:
        print("invalid output! please write a integer between 1 to 20") 
        print("you are left with "+str(9-count)+" attempts")
        count+=1
    num=int(input("input an integer between 1 to 20:-  "))
if num==r_num:
        print("congratulations!🥳🥳🎊🎉🍾🍾🥂🙌\n","you have finished the game in "+str(count)+" attempts.\n"+"This game was created by ABHISHEK VISHAL")