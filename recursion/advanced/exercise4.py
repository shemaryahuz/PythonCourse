def rec_binary(dec):
    if dec == 0:
        return 0
    if dec == 1:
        return 1
    return str(rec_binary(dec // 2)) + str(dec % 2)

def rec_print_binary(dec):
    if dec == 0:
        print(0)
    elif dec == 1:
        print(1, end= "")
    else:
        rec_print_binary(dec // 2)
        print(dec % 2, end= "")

print(rec_binary(17))
rec_print_binary(17)