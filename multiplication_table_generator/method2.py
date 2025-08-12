#Method 2 - F string and for loop with formatting spacing

input_num = int(input("Please enter intput number: "))

for i in range(1,13):
    result = input_num * i
    print(f"{input_num:>2} x {i:>2} = {result:>3}")
