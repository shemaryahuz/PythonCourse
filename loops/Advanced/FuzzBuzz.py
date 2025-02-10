# Run in a loop up to 1,000
# instead of a number divisible by 3, print: Fuzz
# instead of a number divisible by 5, print: Buzz
# instead of a number divisible by both 3 and 5, print: FuzzBuzz

for i in range(1,1001):
    if i%3 == 0 and i%5 == 0:
        print("FuzzBuzz")
    elif i%3 == 0:
        print("Fuzz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)