#Method 1 - F string and for loop

input_num = int(input("Please enter intput number: "))

for i in range(1,13):
  print(f"{input_num} x {i} = {input_num * i}")
