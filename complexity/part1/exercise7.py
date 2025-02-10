#The complexity is linear; O(n), because it depend on the array's length
def find_elements(array,element):
    """Search for a specific element in an array and return its location or a message that it is not found"""
    if element in array:
        return f"{element} is in index {array.index(element)}"
    else:
        return f"{element} is not found"
is_array = [3,4,5,76,78,23,98]
print(find_elements(is_array,75))