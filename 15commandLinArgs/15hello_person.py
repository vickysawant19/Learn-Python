def hello(name, lang):
    greeting = {
        "English" : "hello",
        "Marathi" : "namskar",
        "German" : "hallo",
    }
    msg = f"{greeting[lang]} {name}"
    print(msg)



if __name__== "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="provides a personal greeting"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="name of the person to greet"
    )

    parser.add_argument(
        "-l","--lang",metavar="language",
        required=True,choices=["English","Marathi","German"],
        help="the lang of greeting"
    )

    args = parser.parse_args()

    hello(args.name,args.lang)



