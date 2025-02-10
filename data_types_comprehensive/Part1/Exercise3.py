# Try to create the following dictionaries:
# 1. The keys will be numbers, and their values will be strings
# 2. The keys will be booleans, and their values will be lists.
# 3. The keys will be tuples, and the values will be sets.
# 4. The keys will be sets and the values will be numbers.
# 5. The keys will be lists and the values will be booleans
# 6. The keys will be dictionaries and the values will be strings.

dict_strs = {2:"two",4:"four",6:"six"}
print(dict_strs)
dict_lists = {True:[1,2,3], False:[4,5,6]}
print(dict_lists)
dict_sets = {(1,2,3):{"hello","world"},(4,5,6):{"my","computer"}}
print(dict_sets)
dict_nums = {1:10,4:20}
print(dict_nums)
dict_bools = {1:True,0:False}
print(dict_bools)
dict_strs2 = {1:"first",2:"second"}
print(dict_strs2)