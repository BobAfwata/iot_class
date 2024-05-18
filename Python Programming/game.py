from random import *

rounds_won = 0
for i in range(0,10):
    x = randint(1,10)
    num = int(input("welcome to the game \n Guess a number between 1 and 10: "))
    if num == x:
        print("yay you won!!!")
        rounds_won += 1
        print("\n")
    else:
        print("you lost, boohoo. The answer is {}" .format(x))
        print("\n")
    

print("You won a total of {} rounds" .format(rounds_won))
print("Loading new game...")
import time
time.sleep(5)
import os
os.system("cls")

