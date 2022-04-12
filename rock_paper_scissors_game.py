# take 3 variables rock paper scissors.
# choose randomly any of the three .
# take user input as r, p , or s 
# play the game 10 times 
# display the no of times won 
# display the winner 
import random

print("HI!👋 THERE\nwelcome to the ROCK,PAPER,SCISSORS game\nyou have 10 chances\nthe one with more wins will win the game\nGO ahead and play the game")
objects=["rock","paper","scissors"]
user_won=0
user_lose=0
tie=0
i=0
while i<10:
    comp=random.choice(objects)
    user=input ("\n"+"enter \n'r' for rock\n'p' for paper\n's' for scissors\nENTER HERE:-")

    if user=="r" and comp== "scissors":
        print("you won")
        user_won+=1
    elif user=="r" and comp== "paper":
        print("you lose")
        user_lose+=1
    elif user=="r" and comp== "rock":
        print("tie")
        tie+=1
    elif user=="p" and comp== "rock":
        print("you won")
        user_won+=1
    elif user=="p" and comp== "scissors":
        print("you lose")
        user_lose+=1
    elif user=="p" and comp== "paper":
        print("tie")
        tie+=1
    elif user=="s" and comp== "paper":
        print("you won")
        user_won+=1
    elif user=="s" and comp== "rock":
        print("you lose")
        user_lose+=1
    elif user=="s" and comp== "scissors":
        print("tie")
        tie+=1
    else:
        print("oops! invalid input")
        user_lose+=1
    i+=1

if user_won<user_lose:
    print("\nsorry! you lost the game")
    print("your wins="+str(user_won)+" computer wins="+str(user_lose)+" ties="+str(tie))
elif user_won>user_lose:
    print("\ncongratulations! you won the game")
    print("your wins="+str(user_won)+" computer wins="+str(user_lose)+" ties="+str(tie))
elif user_won==user_lose:
    print("\noops! its a tie... play again!")
    print("your wins="+str(user_won)+" computer wins="+str(user_lose)+" ties="+str(tie))
