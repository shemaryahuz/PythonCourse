# Get a list of words and a word to test
# and return the first position where the word appears
# If the word is not found, return an appropriate message
from operator import index

str_list = []
for i in range(5):
    word = input("Enter a word: ")
    str_list.append(word)
search_str = input("Enter word for searching: ")
if search_str in str_list:
    print(f"{search_str} is in the list at index {str_list.index(search_str)}")
else:
    print(f"{search_str} is not in the list")
