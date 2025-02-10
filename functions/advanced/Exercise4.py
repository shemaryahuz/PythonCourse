def nums_to_asterisks(arr):
    """function that accepts a list of numbers
    and returns a list of strings containing asterisks
    according to the corresponding number in the input list in reverse order."""
    asts_list = []
    for num in arr[::-1]:
        asts_list.append("*" * num)
    return asts_list
help(nums_to_asterisks)
nums_list = [1,2,3,4,5]
print(nums_to_asterisks(nums_list))
