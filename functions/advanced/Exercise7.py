def list_even_indexes(*arr):
    """function that accepts any number of numbers as parameters
    and returns a new list of only the even places in the input list."""
    even_list = []
    for i,num in enumerate(arr):
        if i % 2 == 0:
            even_list.append(num)
    return even_list
help(list_even_indexes)

print(list_even_indexes(31,45,64,32,13,14,24,78))