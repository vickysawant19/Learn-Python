import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(1))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)
# sys.exit()

print(" ")

playerChoice = input("Enter...\n1 for Rock,\n2 for Paper, \n3 for Scissors:\n\n")

player = int(playerChoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2 , 3 ")

computerChoice = random.choice("123")

computer = int(computerChoice)

print("")
print("You chose " + str(RPS(player).name) + ".")
print("Python chose " + str(RPS(computer).name)  + ".")
print("")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player ==  computer :
    print("😲 tie game")
else:
    print("🐍 Python wins!")
