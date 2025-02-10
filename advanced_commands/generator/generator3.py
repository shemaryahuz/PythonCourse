


def non_divided_by_3():
    num = 1
    for i in range(10):
        if num % 3 != 0:
            yield num
            num += 1
        else:
            num += 1

nums = non_divided_by_3()
result = []
for i in range(5):
    result.append(next(nums))
print(result)