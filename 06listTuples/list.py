users = ['vicky','rohan','prakash']
data = ['vicky',29,True]
emptyList = []

print("vicky" in emptyList)

print(users[0])
print(users[-2])

print(users.index('rohan'))

print(users[0:2]) 
# ['vicky', 'rohan']
print(users[-3:-1])
# ['vicky', 'rohan']

print(len(data))

users.append('lala')
print(users)

users += ['json']

users.extend(['robert','jim'])

print(users)

# users.extend(data)  #wecan add that too
# print(users)

users.insert(0,"bob")
print(users)

users[2:2] = ["Elddie","alex"]
print(users)

users[1:3] = ["robert","jPJ"]
print(users)


#remove form list 
users.remove('bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data   # delete whole data
# print(data)

data.clear()
print(data)

#sort list
#users.sort(key=str.lower)
users.sort()
print(users)

nums = [4,34,45,655,32,32]

nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

#change the list withou =t modufying orinfginal

print(sorted(nums,reverse=True))
print(nums)


# create copy of list 
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"neil",True])

print(mylist)

#tuples 

#tuple canot be change

mytuple = tuple(['vicky',24])

anotherTuple = (1,2,3,8)

print(mytuple)
print(type(mytuple))

newlist = list(mytuple)
newlist.append('niel')
newtuple = tuple(mytuple)
print(newtuple)

(one, *two, hey ) = anotherTuple

print(one)
print(two)
print(hey)

print(anotherTuple.count(1))

