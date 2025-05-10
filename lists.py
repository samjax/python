# letters = ['a', 'b', 'c']
# print(letters)
# matrix = [[0,1,2],[3,4,5],[6,7,8]]

# zeros = [0]*5
# combined = matrix + zeros + letters
# print(combined)

# name = 'sampath'
# chars = list(name)
# print(chars)

#lists unpacking
numbers = [1,2,3]
first, second, third = numbers
print(second)

def myfunc(*args):
    first, second, third, *others = args
    print(first)
    print(others)

myfunc(1,2,3,6,7,8,8,9,10)

#enumerate means to take the items in a list or tuple and number them or assign them an index
letters = list('abcdef')
for index, letter in enumerate(letters):
    print(index, letter)


