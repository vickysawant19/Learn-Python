class JustNotCoolError(Exception):
    pass


x= 2

try:
    # raise Exception("im custom exception")
    raise JustNotCoolError("This just isnt cool")
    # print(x/0)
    # if not type(x) is str:
    #     raise TypeError("only strings are allowed ")
except NameError:
    print("NameError means somthing is probaly undefined")
except ZeroDivisionError:
    print("Please do not devide by zero")
except Exception as error:
    print(error)
else:
    print("no error")
finally:
    print("I'm gooing to print with or without error")