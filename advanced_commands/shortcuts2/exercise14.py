from functools import reduce

def long_e_word(words):
    e_words = filter(lambda str: "e" in str, words)
    return reduce(lambda s, w : s if len(s) > len(w) else w, e_words)

strs = ["eli", "hello", "world", "elephant", "big", "employees"]
print(long_e_word(strs))











