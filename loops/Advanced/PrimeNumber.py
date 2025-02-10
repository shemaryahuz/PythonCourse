# Ask the user for a number and print to him whether the number is a prime number.

num = int(input("Please enter a number:"))
is_prime = True
for i in range(2,num):
    if num % i == 0:
        is_prime = False
if is_prime:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")