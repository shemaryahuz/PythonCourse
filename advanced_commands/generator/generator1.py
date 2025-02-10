

def add():
    counter = 1
    while True:
        yield counter
        counter += 1

count = add()
[print(next(count)) for i in range(10)]