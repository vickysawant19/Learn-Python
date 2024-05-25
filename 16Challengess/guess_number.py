import sys
import random

def guess_number(name = 'playerOne'):
    guessed_number = 0
    game_count = 0
    player_win = 0
    computer_win = 0

    def play_game():
        nonlocal guessed_number
        nonlocal game_count
        nonlocal computer_win
        nonlocal player_win
        
        print(f"{name},Welcome!\n")

        computer_number = random.choice([1,2,3])

        guessed_number = int(input(f"{name},Guess the number i am thinkg ! 1,2 or 3\n"))

        if guessed_number not in [1,2,3]:
            print(f"\n{name}, Please enter 1, 2 , 3 ")
            return play_game()

        game_count += 1

        if computer_number == guessed_number:
            print(f"\n{name} win, you guessed it right")
            player_win +=1
        else:
            print(f"\ncomputer win!,your guess was wrong")
            computer_win +=1

        print(f"\n{name} chose {guessed_number}.")
        print(f"\nComputer chose {computer_number}.\n")
        

        print(f"\nGame Count :{game_count}")
        print(f"\n{name} wins :{player_win}")
        print(f"\nComputer wins :{computer_win}")

        print(f"\nWining percentage is {player_win/game_count:.2%}")

        while(True):
            play_again = (input("\nWant to play again?\nY for yes or\nQ for quit\n")).lower()
            if play_again.lower() not in ["y","q"]:
                continue
            else:
                break

        if play_again == "y":
            return play_game()
        else:
            print("\n🏆🏆🏆🏆🏆")
            print("\n🥳 Thank you!")
            if __name__ == "__main__":
                sys.exit(f"Bye,{name}!! 👋")
            else:
                return

    return play_game

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="provides a personalized game exprience"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="name of the person playing the game"
    )

    args = parser.parse_args()

    game1 = guess_number(args.name)
    game1()


