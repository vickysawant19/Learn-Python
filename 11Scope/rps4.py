import sys
import random
from enum import Enum


game_count = 0

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

    def decide_winner(player,computer):
        if player == 1 and computer == 3:
            return "🎉You win!"
        elif player == 2 and computer == 1:
            return "🎉You win!"
        elif player == 3 and computer == 2:
            return "🎉You win!"
        elif player ==  computer :
            return "😲 tie game"
        else:
            return "🐍 Python wins!"
    

    game_result = decide_winner(player,computer)
    print(game_result)

    global game_count
    game_count += 1
    print("\nGame Count : "+ str(game_count))

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

