
def dict_parameters(**arr):
    """function that accepts any number of named parameters
    and returns a dictionary with the parameter names as the key
    and the parameter values as the values of the returned dictionary."""
    is_dict = arr
    return is_dict

new_dict = dict_parameters(one = 1, two = 2, three = 3, four = 4, five = 5)

print(new_dict)