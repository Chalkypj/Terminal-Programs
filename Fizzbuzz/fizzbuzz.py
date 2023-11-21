""" Simple FizzBuzz progaram - Prints the numbers from 0 to 100. 
	Assigns Fizz if divisible by 3, Buzz is divisible by 5 and 
	FizzBuzz if divisible by 3 and 5
"""

for i in range(0, 101):
    if i != 0:
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} Fizz")
        elif i % 5 == 0:
            print(f"{i} Buzz")
        else:
            print(i)
    else:
        print(i)
