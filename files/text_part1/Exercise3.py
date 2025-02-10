
def fifty_chars(filename):
    f = open(filename, "r")
    chars = f.read()[0:50]
    f.close()
    return chars

file = open("exercise3.txt", "a")

for i in range(10):

    file.write("abcd\n")

file.close()

print(fifty_chars("exercise3.txt"))


