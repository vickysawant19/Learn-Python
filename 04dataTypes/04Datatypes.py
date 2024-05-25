#String data types


#Literal aassignment 

first = "vicky"
last = "sawant"

# print(type(first)) # <class 'str'>
# print(type(first) == str) #true
# print(isinstance(first,str)) #true


#constructor

# pizza = str('Pepperoni')
# print(type(pizza)) # <class 'str'>
# print(type(pizza) == str) #true
# print(isinstance(pizza,str)) #true

#Concatination

# fullname = first +" " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# #casting number to string

# decade = str(1990)
# print(type(decade))
# print(decade)

# statement = "i like music "+ decade + " of this decade"

# print(statement)

# #Multiple lines

multiline = '''
Hey,how are yor?

I was just checking in ..

All good

'''
# print(multiline)

#escaping special character

sentence = 'i\'m good! \tHey!\n\nwhere\'s this at\\located?'
print(sentence)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())  #Make A Change Like This

print(multiline.replace("good","ok"))

print(len(multiline))
multiline += "                                "
multiline = "                     " + multiline

print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# build a menu 

title = "menu".upper()
print(title.center(20,"="))

print("Coffee".ljust(16,".")+ "$1".rjust(4))
print("Muffin".ljust(16,".")+ "$2".rjust(4))
print("ChiseCake".ljust(16,".")+ "$4".rjust(4))

#String indexx values

print(first[1])  #Vicky  gives i
print(first[-1])  #Vicky  gives y last letter
print(first[1:-1])  #Vicky  gives   ick  
print(first[1:])  #Vicky  gives icky last letters


#some methods return boolean

print(first.startswith('D')) #false
print(first.startswith('v')) #true
print(first.endswith('y')) #true

#Boolean data types

myvalue = False
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric data types
#integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price,int))
#floot
gpa =3.28
y = float(1.13)
print(type(gpa))

#complex  type
comp_value = 5+3j

print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)