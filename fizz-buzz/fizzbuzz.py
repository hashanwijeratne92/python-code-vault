def fizzbuzz(count):
    results = []

    for i in range(1, count+1):
        #number dividing by 3 and 5
        if i % 15 == 0:
            results.append("FizzBuzz")
        #number dividing by 3
        elif i % 3 == 0:
            results.append("Fizz")
        #number dividing by 5
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(i)
    return results

print(fizzbuzz(100))
