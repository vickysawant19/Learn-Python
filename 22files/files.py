#read = error if doesnt exit


f = open("names.txt",'r')
# print(f.read())
# print(f.read(5))

# print(f.readline()) # read first line
# print(f.readline())  #read 2nd line 

# for line in f:
#     print(line)

# f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print(f"file doent exits") 
finally:
    f.close()

#Append - create the file if it doens exists

f = open("names.txt","a")
f.write("vijay\n")
f.close()

f = open('names.txt')
print(f.read())
f.close()

#Write (overwrite)

f = open('context.txt','w')
f.write('i deleted all of the contexxt')
f.close()

f = open('context.txt')
print(f.read())
f.close()


#two ways to create a new file

#opens a file for writing ,,create the file if it does not exits

f = open('name_list.txt','w')
f.close()

#crete sppecified file but returns a specified error if the file exists 
import os

if not os.path.exists('vicky.txt'):
    f= open('vicky.txt','x')
    f.close()


# delete a file 

#avoid a error if it doents exits
print(os.path.exists("vicky.txt"))

if os.path.exists("vicky.txt"):
   
    os.remove('vicky.txt')
else:
    print('file does not exists ')

with open('more_names.txt') as f:
    content = f.read()
    f.close()

with open('names.txt','w') as f:
    f.write(content)
    f.close()