#closer is a functionn having access to scope of its parents function after the parrent function has returned


def parent_fn(person,coins):
    #coins = 3

    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has "+ str(coins) + " coins left")
        elif coins == 1:
            print("\n" + person + " has "+ str(coins) + " coin left")
        else:
            print("\n" + person + " has " + " is out of coin")

    return play_game

tommy = parent_fn("Tommy",3)
jinny = parent_fn("Jinny",2)

tommy()
tommy()

jinny()

tommy()