name = "vicky"  #global scope




# greeting("john")
# print(color)  does not have access
count = 1


def another():
    global count
    count += 2
    color = "blue" 
    def greeting(name):    #global scope
        print(name)   # use args
        print(color)
        print(count)

    greeting("john")


another()