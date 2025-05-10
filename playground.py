# age = input("enter your age: ")
# gender = input("M or F? :")

# if int(age) < 15 and gender == 'F': 
#     print("you are a girl younger than 15!")
# elif int(age) == 15 and gender == 'M':
#     print("you are 15 yo male")
# else:
#     print("you didn't match the criteria")

# for i in range(0,10,9):
#     print(f'Current value of i: {i}')

# while 3<5:
#     print('True')

# nameList = ['sampath', 'kumar', 34]
# print(nameList[-1])
# nameList.append('elon')
# print(nameList)
# nameList[-1] = 'Musk'
# print(nameList)
# print(type(nameList))

# color=(234,23,43)
# print(type(color))

#string methods

# a = " adskf "
# a.strip()
# print(a.strip())

# sentence = "I am a great programmer"
# list_of_words = sentence.split(" ")
# print(list_of_words)

#SLICE operator

# name = "sampath"
# print(name[1:4])


# nameList = ['sampath', 'kumar', 34]
# nameList.insert(2,"newname")
# print(nameList)

# nameList[2:2] = 'abc'

# print(nameList)

# nameList[3:2] = ['abc']

# print(nameList)

#FILE operations

# file = open('sampath.txt', 'r')
# f = file.readlines()
# newList = []
# print(f)

# for line in f:
#     newList.append(line)
# print(newList)

#writing to a file
# file = open('file.txt', 'w')

# file.write("My name is:\n")
# file.write("This will be on a new line")

# file.close()

#find() and count() methods

#this can be used to find a character in a string..can it be used to search a list?

name = 'sampath'
print(name.find('h'))

print(name.count('s'))

nameList = ['sampath', 'kumar', 34]
print(nameList.index(34))