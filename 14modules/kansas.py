from random import choice

bird = "forest meadowlark"

flower = "sunflower"

song = "Home on the Range"

capital =   "Home on the range"

def randomFunfact():
    funfact = [ "kanas is considerd  flat , but it dooes have a moutain.",
               "wichita is the largerst city in the stat, but many would guess that it is kanas city",
               "A considerable portion of kanas city is actually in missouri."]
    
    index  = choice("012")

    print(funfact[int(index)])


# its needed otherwise import will call this
if __name__ == "__main__":
    randomFunfact()