"""Final Exam"""


"""code analysis"""
def f(x):
    y = []
    while x:
        tmp = x.pop()
        while y and y[-1] > tmp:
            x.append(y.pop())
        y.append(tmp)
    return y
# a = [12, 9, 35, 7]
# a = f(a)
# print(a)

"""Theme Park"""
from random import randrange
class RollerCoaster:
    def __init__(self, type):
        self.type = type
        self.carriages = randrange(1,20)

    def get_ride_time(self):
        if self.type == "Regular":
            return 60 * self.carriages
        return 30 * self.carriages
class ThemePark:
    def __init__(self):
        self.roller_coaster_lst = []
        for i in  range(1, 51):
            if i % 5 == 0:
                self.roller_coaster_lst.append(RollerCoaster("Extreme"))
            else:
                self.roller_coaster_lst.append(RollerCoaster("Regular"))
    def print_rides(self):
        for i, rol in enumerate(self.roller_coaster_lst):
            print(f"Roller coaster number: {i+1}\n"
                  f"Type: {rol.type}\n"
                  f"Number of carriages: {rol.carriages}\n"
                  f"Ride time: {rol.get_ride_time()}")
# park = ThemePark()
# park.print_rides()

"""optimized sort"""
def optimized_sort(lst):
    for i in range(len(lst)-1):
        is_sorted = True
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                is_sorted = False
        if is_sorted:
            break
    return lst

# a = [6,3,2,1,5,4]
# print(optimized_sort(a))

"""Sum of digits"""
def sum_of_digits(num):
    if num < 10:
        return num
    return sum_of_digits(num//10) + num % 10

# number = 541
# print(sum_of_digits(number))

"""Sum min"""
def sum_min(root):
    if not root:
        return 0
    return root.value + sum_min(root.left)

"""Sum tree"""
def sum_tree(root):
    if not root:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)