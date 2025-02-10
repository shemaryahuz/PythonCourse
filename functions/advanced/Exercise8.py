
def solve_quadratic_equation(a, b, c):
    """function that accepts 3 parameters a, b, c.
    which are the coefficients of a quadratic equation of the form:
    ax^2 + bx + c = 0.
    and returns the roots of the equation."""
    solutions = ""
    discriminant = (b ** 2 - 4 * a * c)
    if discriminant < 0:
        solutions += "The equations has no real solution"
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        if discriminant == 0:
            solutions += "x = " + str(root1)
        else:
            solutions += "x1 = " + str(root1)
            solutions += ", x2 = " + str(root2)
    return solutions

help(solve_quadratic_equation)

A = float(input("Enter coefficient a: "))
B = float(input("Enter coefficient b: "))
C = float(input("Enter coefficient c: "))
print(solve_quadratic_equation(A,B,C))