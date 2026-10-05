CORRECT_PASSWORD = "MyPassword"
attempts = 0

while True:
    password = input("Please type your password: ")
    attempts += 1

    if password == CORRECT_PASSWORD:
        print("User is logged in")
        break

    else:
        if attempts == 3:
            print("User account is blocked")
            break
        else:
            print("Incorrect password. Please try again.")