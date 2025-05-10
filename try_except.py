text = input('Username: ')
try:
    number = int(text)
    print(number)
except:
    print("invalid user name")