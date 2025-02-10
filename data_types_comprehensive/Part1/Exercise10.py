# Create a dictionary with 5 items, replacing the keys with values and the values with keys.

is_dict = {1:"one",2:"tow",3:"three",4:"four",5:"five"}
copy_dict = is_dict.copy()

for key,val in copy_dict.items():
    is_dict[val] = key
    is_dict.pop(key)

print(is_dict)