

def compare_files(file1, file2):
    try:
        f1 = open(file1)
        txt1 = f1.read()
        f1.close()
        f2 = open(file2)
        txt2 = f2.read()
        f2.close()
        return txt1 == txt2
    except FileNotFoundError :
        print("File not found")

print(compare_files("exercise6_a","exercise6_b"))












