import sys
import random
from enum import Enum

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3


    playerChoice = input("Enter...\n1 for Rock,\n2 for Paper, \n3 for Scissors:\n\n")
    
    if(playerChoice not in ["1","2","3"]):
        print("\nYou must enter 1, 2 , 3 ")
        return play_rps()


    player = int(playerChoice)

    computerChoice = random.choice("123")

    computer = int(computerChoice)


    print("You chose " + str(RPS(player).name) + ".")
    print("Python chose " + str(RPS(computer).name)  + ".\n")


    if player == 1 and computer == 3:
        print("🎉You win!")
    elif player == 2 and computer == 1:
        print("🎉You win!")
    elif player == 3 and computer == 2:
        print("🎉You win!")
    elif player ==  computer :
        print("😲 tie game")
    else:
        print("🐍 Python wins!")
    
    print("\nPlay again ?")

    while(True):
        playAgain = input(" \nY for Yes\nQ for Quit \n\n")
        if playAgain.lower() not in ["y","q"]:
            continue
        else:
            break

    if playAgain.lower() == "y":
        return play_rps()
    else:
        print("\n🥳 Thank you!")
        sys.exit("Bye!!")
       


play_rps()

