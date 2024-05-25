

squared = lambda num : num * num

print(squared(2))

addtwo = lambda num : num + 2

print(addtwo(10))

sum_total =lambda a,b : a+b

print(sum_total(2,3))

##########################################

def funcBuilde(x):
    return lambda num: num+x


add10 = funcBuilde(10)
add20 = funcBuilde(20)

print(add10(4))
print(add20(10))

##Higher order func


lambda num : num * num

numbers  = [2,4,5,23,12]

squerd_num = map(lambda num: num * num ,numbers)

print(list(squerd_num))

#######################

lambda num: num % 2 != 0

odd_num = filter(lambda num: num % 2 != 0,numbers)

print(list(odd_num))

##########

from functools import reduce

lambda acc,current: acc +current

numbers = [1,2,3,4,5,1]


print(sum(numbers,10))  # simple solutioon addd array numbers fives 26


total =reduce(lambda acc,current: acc +current,numbers ,10)

print(total)



lambda acc,curr: acc +len(curr)

names = ['vicky','sawant','john','jackup','sarahh']

char_count = reduce(lambda acc,curr: acc +len(curr),names,0)

print(char_count)