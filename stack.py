#program to simulate a stack

i = 0
browsing_sessions = []
while True:
    i += 1
    print(browsing_sessions)
    user_response = input('Do you want to conntinue? : ')
    if user_response == 'y' or user_response == 'Y':
        browsing_sessions.append(i)
    elif user_response == 'n' or user_response == 'N':
        if browsing_sessions:
            browsing_sessions.pop()
        else:
            break


