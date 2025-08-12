# Method3 - for loop and f string with try-except

try:
    number = int(input("Please enter Integer number: "))
    if number <= 0:
        print("Please enter positive integer number")
    else:
        for i in range(1,13):
            result = number * i
            print(f"{number:>2} x {i:>2} = {result:>3}")

except ValueError:
    print("Input error! Please enter valid integer number.")

