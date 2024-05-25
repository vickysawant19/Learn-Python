person = "vicky"
coins = 3

print("\n" + person + " has " + str(coins)+ " coins left")

message = "\n%s has %s coins left." % (person,coins)
print(message)

message = "\n{} has {} coins left.".format(person,coins)
print(message)

message = "\n{0} has {1} coins left.".format(person,coins)
print(message)


player = { "person": "vicky" , "coins": 3}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

############
# f- string ! this is a way!
message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*10} coins left."
print(message)

message = f"\n{person.upper()} has {coins} coins left."
print(message)

message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

#you can pass formatting options

num = 10
print(f"\n2.24 times {num} is {2.24 * num:.2f}\n")


for num in range(1,11):
    print(f"2.24 times {num} is {2.24 * num:.2f}")


for num in range(1,11):
    print(f"{num} divided bt 4.23 is {num / 4.23:.2%}")