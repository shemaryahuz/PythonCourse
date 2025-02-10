

def generate_numbers():
    for i in range(3):
        yield i

gen = generate_numbers()
print(next(gen))
print(next(gen))

# output:
# 0
# 1








