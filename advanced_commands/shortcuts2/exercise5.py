
def a_strs(strs):
    return list(filter(lambda s: len(s) > 0 and s[0] == "a", strs))


strs_list = ["banana", "a", "apple", "hey","" ,"avi", "aba"]
print(a_strs(strs_list))




