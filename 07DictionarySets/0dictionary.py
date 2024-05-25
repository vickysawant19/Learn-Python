#Dictionary


band = {
    "vocals" : "plant",
    "guitar" : "page"
}
band2 = dict(vocals = "plant" ,guitar = "page")

print(band)
print(band2)

print(type(band))
print(len(band))

#access items

print(band["guitar"])
print(band.get('guitar'))

#list all keys 
print(band.keys())

#list all values

print(band.values())


# list of key value as pairs of tuples

print(band.items())

print("guitar" in band) #true

band['vocals'] = "coverdale"

print(band)

band.update({'bass':"JPJ"})
print(band)

#remove items

print(band.pop('bass'))
print(band)

print(band.popitem()) # return tuple
print(band)

#delete

del band["vocals"]
print(band)

band2.clear()
print(band2)

del band2


#copy dict

#bad copy
# band2 = band #create refrence



band2 = {
    "1" :"one",
    "2" :"two"
      }
#good copy

# band = band2.copy()
# print(band2)
# print(band)

# or use dict ()

band = dict(band2)
print(band2)
print(band)


#nested dict

member1 = {
    "name" : "vicky",
    "instrument" : 'vocals'
}


member2 = {
    "name" : "rohan",
    "instrument" : 'guriter'
}

band = {
    "member1": member1,
    "member2" :member2,
}
print(band)
print(band)
print(band["member1"]['name'])

#set

nums = {1,2,3,4}

nums2 = set({1,2,3,4,5})

#no dupicates
nums = {1,2,2,3}
print(nums)

nums = {1,True,2,False,0}
print(nums)

#check value in set

print(2 in nums)

#add elemt

nums.add(9)
print(nums)

#add element from one set to another

morenums = {5,6,7}
nums.update(morenums)
print(nums)  #{False, 1, 2, 5, 6, 7, 9}