def hello():
    print("hello world!")

hello()

def sum(num1= 0,num2 = 0):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1+num2

# sum(20,20)
# sum(20,50)
# sum(20,60)

total = sum(3,4)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("dev","john","sarah")
#######


def mul_names_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mul_names_items(first = "dave",second = "john",last="vikcy")
# {'first': 'dave', 'second': 'john', 'last': 'vikcy'} 
# <class 'dict'>