# Create a dictionary with 30 items where all values are numbers.
# Loop through and for even values print:
# A. The key name
# B. The value


dict_numbers = {}
for i in range(1,31):
    dict_numbers[i] = i
print(dict_numbers)

for key,value in dict_numbers.items():
    if value % 2 == 0:
        print(key,value)