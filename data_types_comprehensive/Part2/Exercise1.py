# Write code that reverses the keys and the values will be reversed with the following condition:
# In case there is a value that appears several times, all its keys should be saved
# as a list.

is_dict = {}

copy_dict = is_dict.copy()

for key,val in copy_dict.items():
    is_dict[val] = key
    is_dict.pop(key)

print(is_dict)