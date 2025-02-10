# Show the user the following menu:
# A. Login to the system
# B. Create a user
# C. Exit the system

# If the user chose A:
# 1. Ask him for the username (display an error message accordingly)
# 2. Ask him for the password (up to 3 attempts for a correct password)
# He must be allowed to return to the main menu at any stage by inserting an asterisk *.

# After entering the system, a greeting message and the following menu must be printed:
# A. print text to it (a string you saved at the beginning of the program, whatever you want)
# B. change password
# C. Delete the user
# D. Exit the system and return to the main menu
# E. Log out completely

# If the user chose B:
# 1. He should be asked to choose a username (the username will be his ID.).
# 2. The user must be asked to choose a password
# He must be allowed to return to the main menu at any stage by inserting an asterisk *.

# If the user chose C, the system must be exited.


users = {}
to_break = False
while not to_break:
    print("USER SYSTEM")
    print("A: Login to the system")
    print("B: Create a account")
    print("C: Exit the system")
    print("(At each step enter an asterisk * to return to the main menu)")
    print()
    print()
    print()
    choice = input("Chose A/B/C: ")
    if choice == "*":
        print()
        print()
        print()
        continue

    if choice == "A":
        username = input("Enter your username: ")
        if username == "*":
            print()
            print()
            print()
            continue
        if username in users:
            password = input("Enter the password: ")
            if password == "*":
                print()
                print()
                print()
                continue
            if users[username] == password:
                print("Welcome to our system!")
                print("Options:")
                print("1: Change password")
                print("2: Delete account")
                print("3: Exit the system")
                print()
                print()
                print()
                choice = input("Choose 1/2/3: ")
                if choice == "*":
                    print()
                    print()
                    print()
                    continue
                if choice == "1":
                    new_password = input("Enter the new password: ")
                    if new_password == "*":
                        continue
                    users[username] = password
                    print("Your password changed successfully!")
                if choice == "2":
                    users.pop(username)
                    print("The account deleted successfully!")
                    print()
                    print()
                    print()
                elif choice == "3":
                    break
            else:
                for i in range(2):
                    print("Wrong password, try again")
                    password = input("Enter the password: ")
                    if password == "*":
                        break
                    if users[username] == password:
                        print("Welcome to our system!")
                        print("Options:")
                        print("1: Change password")
                        print("2: Delete account")
                        print("3: Exit the system")
                        choice = input("Choose 1/2/3: ")
                        if choice == "*":
                            break
                        if choice == "1":
                            new_password = input("Enter the new password: ")
                            if new_password == "*":
                                break
                            users[username] = password
                            print("Your password changed successfully!")
                            print()
                            print()
                            print()
                            break
                        if choice == "2":
                            users.pop(username)
                            print("The account deleted successfully!")
                            print()
                            print()
                            print()
                            break
                        elif choice == "3":
                            to_break = True

    elif choice == "B":
        username = input("Enter a username: ")
        if username == "*":
            print()
            print()
            print()
            continue
        password = input("Enter a password: ")
        if password == "*":
            print()
            print()
            print()
            continue
        users[username] = password
        print("Your account created successfully!")
        print()
        print()
        print()
        continue

    elif choice == "C":
        break