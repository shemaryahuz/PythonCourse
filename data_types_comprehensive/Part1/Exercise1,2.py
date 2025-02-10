# 1. Create a set of booleans, a set of integers, a set of real numbers, and a set of strings (with at least 2 elements).
# 2. Try to print specific elements in the sets, and also try to add elements that already exist in a certain set add() can be used.

set_booleans = {True, False}
print(set_booleans)
set_ints = {4,8,5}
print(set_ints)
set_floats = {1.5,2.25,8.75}
print(set_floats)
set_strs = {"hello","bye","world"}
print(set_strs)
x = set_booleans.pop()
print(x)
y = set_ints.pop()
print(y)
z = set_floats.pop()
print(z)
q =  set_strs.pop()
print(q)
set_ints.add(80)
print(set_ints)
set_floats.add(10.2)
print(set_floats)
set_strs.add("my")
print(set_strs)