# Create an empty list called numbers and fill it with 100 consecutive numbers, using the shortest code.
# Then print all the elements from the end to the beginning.

numbers = []
for i in range(100):
    numbers.append(i + 1)
print(numbers[100::-1])