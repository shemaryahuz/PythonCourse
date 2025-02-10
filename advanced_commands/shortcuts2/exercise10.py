
def print_odd_indexes(str):
    [print(str[i], end= " ") for i in range(len(str)) if i % 2 == 0]

print_odd_indexes("aabbccddeeffgghhjj")




