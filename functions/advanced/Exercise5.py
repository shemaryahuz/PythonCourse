
def sum_couple(a,b):
    """function that will accept two numbers and return their sum."""
    return a + b
help(sum_couple)

def multiply_couple(c,d):
    """function that will accept two numbers and return their multiplication."""
    return c * d
help(multiply_couple)

def list_sum_and_multy(num):
   """ function that accepts a number
   and returns a list with the following values:
    - The product of the number we entered by the number that follows it.
    - The sum of the number we entered and the number that follows it.
    - The product of the number we entered by the number that precedes it.
    - The sum of the number we entered and the number that precedes it."""
   multy_fallow = multiply_couple(num,num + 1)
   sum_fallow = sum_couple(num, num + 1)
   multy_pre = multiply_couple(num, num - 1)
   sum_pre = sum_couple(num, num - 1)
   is_list = [multy_fallow,sum_fallow,multy_pre,sum_pre]
   return is_list
help(list_sum_and_multy)

print(list_sum_and_multy(5))