#Method - Using for loop and range

correct_password = "python123"

for attempts in range(3):
    guess_passwd = input("Please enter valid password: ")
    
    if guess_passwd == correct_password:
        print("Access granted!")
        break
    else:
        print("Password Incorrect. Try again.")

else:
    print("Too many attempts. You are locked out.")
