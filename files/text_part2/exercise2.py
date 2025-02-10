

def print_file(file):

    f = open(file)
    line = f.readline()
    while line:
        if line[-1] == "\n":
            print(f"length: {len(line[:-1])}. text: {line}", end="")
        else:
            print(f"length: {len(line)}. text: {line}")
        line = f.readline()
    f.close()

print_file("exercise2")