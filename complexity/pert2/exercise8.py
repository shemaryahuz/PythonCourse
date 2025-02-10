# Calculate the exact runtime complexity and order of magnitude of each function

def fun(n):
    for i in range(n):
        print(i * n)
# The exact runtime complexity is: 3n. and the order of magnitude of the complexity is: O(n).


def fun_time(n):
    k = 0
    for i in range(n):
        for j in range(n // 2):
            k += 1
            print(i + j)
# The exact runtime complexity is: n * (n/2 + 4) + 1. and the order of magnitude of the complexity is: O(n).


def very_fun_time(n):
    k = 0
    i = 1
    while i < n:
        j = 1
        while j < n / 2:
            k += 1
            print(i * j)
            j *= 4
        i *= 2
# The exact runtime complexity is: log n * (log (log n // 2) + 6) + 5. and the order of magnitude of the complexity is: O(log n).


def not_very_fun_time(n):
    k = 0
    for i in range(n):
        for j in range(i):
            k += 1
            print(i * j)
            k -= 1
# The exact runtime complexity is: n * (n + 6) + 1. and the order of magnitude of the complexity is: O(n ** 2).


def cool_time(n):
    i = 2
    while i < n:
        i *= i
# The exact runtime complexity is: log n + 3. and the order of magnitude of the complexity is: O(log n).


def very_cool_time(n):
    for i in range(n):
        for j in range(i):
            while i < n:
                print(i * i)
# The exact runtime complexity is: n * (n * (log n + 2)) . and the order of magnitude of the complexity is: o(n ** 2).


def cool_with_time(n):
    i = 2
    while i < n:
        n //= 2
# The exact runtime complexity is: log n + 3. and the order of magnitude of the complexity is: O(log n).