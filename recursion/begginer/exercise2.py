def rec_print_num(num):
    print(num)
    rec_print_num(num + 1)

rec_print_num(0)