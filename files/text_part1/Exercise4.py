

def write_text(filename,str):

    try:
        f = open(filename, "a")
        f.write(f" {str}")
        f.close()
        return True
    except:
        print("not allowed")
        return False
# def write_text(filename):
#
#     with open(filename, "w") as f:
#         f.write("hello")

# file = open("exercise4.txt", "x")
a = write_text("exercise4.txt","Hello")
b = write_text("exercise4.txt","World")
print((a, b))