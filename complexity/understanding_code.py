# Calculate for each function:
# A. What is the number of *operations* the function performs? (operation = print, return)
# B. What is the order of magnitude of the function's runtime?


# function 1
def func1(n):
    return n + 1
# A. n
# B. O(n)

# function 2
def func2(arr):
    for i in arr:
        print(i)
# A. 2n
# B. O(n)

# function 3
def func3(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
# A. n ** 2
# B. O(n ** 2)

# function 4
def func4(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)
# A. n ** 3
# B. O(n ** 3)

# function 5
def func5(n):
    i = 1
    while i < n:
        print(i)
        i *= 2
# A. log n
# B. O(log n)

# function 6
def func6(arr):
    for i in arr:
        for j in range(len(arr)):
            print(i, j)
# A. n ** 2
# B. O(n ** 2)

# function 7
def func7(n):
    for i in range(n):
        for j in range(i, n):
            print(i, j)
# A. n ** 2
# B. O(n ** 2)

# function 8
def func8(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
# A. 2n
# B. O(n)

# function 9
def func9(n):
    i = n
    while i > 1:
        print(i)
        i = i // 2
# A. log n
# B. O(log n)

# function 10
def func10(n):
    for i in range(n):
        for j in range(int(n**0.5)):
            print(i, j)
# A. n * (log n)
# B. O(n ** 2)

# function 11
def func11(n):
    if n <= 1:
        return 1
    return func11(n - 1) + func11(n - 2)
# A.
# B.

# function 12
def func12(n):
    if n <= 1:
        return
    for i in range(n):
        print(i)
    func12(n // 2)
# A.
# B.

# function 13
def func13(n):
    for i in range(n):
        print(i)
    for j in range(2 * n):
        print(j)
# A. 3n
# B. O(n)

# function 14
def func14(n):
    for i in range(n):
        print(i)
    for j in range(n):
        for k in range(10):
            print(j, k)
# A. 11n
# B. O(n)

# function 15
def func15(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                print(i, j, k)
# A. n ((n/2) * (n/4))
# B. O(n ** 2)

# function 16
def func16(arr):
    n = len(arr)
    for i in range(n):
        print(i)
    for j in range(n):
        for k in range(j, n):
            print(j, k)
# A. n + n * (n/2)
# B. O(n ** 2)

# function 17
def func1function7(n):
    i = 1
    while i < n:
        for j in range(i):
            print(j)
        i *= 2
# A. log n ** 2
# B. O(log n)

# function 18
def func18(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                print(i, j)
# A.
# B.

# function 19
def func19(n):
    i = n
    while i > 1:
        for j in range(i):
            print(j)
        i = i // 2
# A.
# B.

# function 20
def func20(arr):
    for i in range(len(arr)):
        print(arr[i])
    if len(arr) > 1:
        func20(arr[1:])
# A.
# B.
