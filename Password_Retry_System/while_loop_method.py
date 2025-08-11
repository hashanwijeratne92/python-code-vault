#While loop method

correct_password = "python123"
attempts = 0

while attempts < 3:
    guess_pass = input("Please enter valid password: ")
    attempts += 1

    if guess_pass == correct_password:
        print("Access Granted!")
        break
    else:
        print("Incorrect Password. Try again.")

if attempts == 3:
    print("Too many attempts. You are locked out!")

