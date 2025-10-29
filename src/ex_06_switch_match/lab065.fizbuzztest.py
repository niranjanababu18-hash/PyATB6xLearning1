#number from 1 to 100.
# if multiple of 3-print fizz
# if number multiple of 5,print buzz,
# if multiples of both-print'fizzBuzz"
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

