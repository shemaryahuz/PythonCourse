

def rec_print_str(str):
    print(str)
    rec_print_str(str[:-1])

rec_print_str("qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuio")