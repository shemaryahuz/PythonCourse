
def lines_arr(filename, str):
    file = open(filename)
    lines = file.readlines()
    file.close()
    selected_lines = []
    for line in lines:
        if line[0:len(str)] == str:
            if line[-1] == "\n":
                selected_lines.append(line[0:-1])
            else:
                selected_lines.append(line)
    return selected_lines


f = open("exercise5.txt")
h_strs = lines_arr("exercise5.txt", "H")
hello_strs = lines_arr("exercise5.txt", "Hello")
print(f"{h_strs}\n{hello_strs}")
