import sys 
import rps
import guess_number


def arcade(name):

    def chose_game():
    
        print(f"\n{name} Please enter 1,2 or x\n\n")

        game = input(f"Please chose game:\n1 = Rock paper Scissors\n2 = Guess my number\n\n Or press 'X' to exit the arcade\n\n")


        if game not in ["1","2","x"]:
            return chose_game()
        elif game == "1":
            game1 = rps.rps(name)
            game1()
            return chose_game()
        elif game == "2":
            game2= guess_number.guess_number(name)
            game2()
            return chose_game()
        else:
            print("\n🥳 Thank you!")
            sys.exit(f"Bye,{name}!!")

    return chose_game


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

    

    gameOne= arcade(args.name)
    gameOne()
