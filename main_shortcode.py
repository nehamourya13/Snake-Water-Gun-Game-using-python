'''
Snake = 1
water = -1
gun = 0 '''
import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(f"computer chose {reverseDict[computer]}\nYou Chose {reverseDict[you]}")

'''
   else:
    if(computer == -1 and you == 1): -2
       print("You win!")
    elif(computer == -1 and you == 0): -1
       print(" You lose")
    elif(computer == 1 and you == 0): 1
       print("You win!")
    elif(computer == 1 and you == -1): 2
       print("You lose!")
    elif(computer == 0 and you == -1): 1
       print("You win!")
    elif(computer == 0 and you == 1): -1
       print("You lose!")
    else:
       print("Something went wrong")'''
if ((computer - you) == -1 or (computer - you) == 2):
    print("You Lose!")

elif (computer == you):
    print("Its'a a Draw!")
else:
    print("You win!")
