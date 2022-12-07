# FizzBuzz
# Program Details:
#   -> divisible by 3, print Fizz.
#   -> divisible by 5, print Buzz.
#   -> divisible by both 3 & 5, print FizzBuzz
#   -> if divisible by none, print the number as it is.

#Solution

for i in range(100):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)