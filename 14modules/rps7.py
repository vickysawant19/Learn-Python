import sys
import random
from enum import Enum



def rps():
    game_count = 0
    player_win = 0
    python_win = 0

    def play_rps():
        nonlocal player_win
        nonlocal python_win

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

        print(f"You chose {str(RPS(player).name)}.")
        print(f"Python chose {str(RPS(computer).name)}.")

        def decide_winner(player,computer):
            nonlocal player_win
            nonlocal python_win
            if player == 1 and computer == 3:
                player_win += 1
                return "🎉You win!"
            elif player == 2 and computer == 1:
                player_win += 1
                return "🎉You win!"
            elif player == 3 and computer == 2:
                player_win += 1
                return "🎉You win!"
            elif player ==  computer :
                return "😲 tie game"
            else:
                python_win += 1
                return "🐍 Python wins!"
        

        game_result = decide_winner(player,computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count :{str(game_count)}")
        print(f"\nPlayer wins :{str(player_win)}")
        print(f"\nPython wins :{str(python_win)}")

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

    return play_rps
        

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()



