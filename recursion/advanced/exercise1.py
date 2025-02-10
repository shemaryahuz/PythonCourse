def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    number = 6
    print(f"The {number}th Fibonacci number is: {fibonacci(number)}")

"""
The function accepts a number representing the number of elements in the Fibonacci series from 1 to n,
and returns the element at position n.

Example explanation:

fibonacci(n = 6):
                |    
                |____fibonacci(n = 5):
                |                    |
                |                    |____fibonacci(n = 4):
                |                    |                    |
                |                    |                    |___fibonacci(n = 3):
                |                    |                    |                   |
                |                    |                    |                   |___fibonacci(n = 2):
                |                    |                    |                   |                   |
                |                    |                    |                   |                   |___fibonacci(n = 1):
                |                    |                    |                   |                   |                   |___return 1
                |                    |                    |                   |                   |
                |                    |                    |                   |                   |___fibonacci(n = 0):
                |                    |                    |                   |                   |                   |___return 0
                |                    |                    |                   |                   |  
                |                    |                    |                   |                   |___return 1 + 0 [=1]
                |                    |                    |                   |  
                |                    |                    |                   |___fibonacci(n = 1):
                |                    |                    |                   |                   |___return 1
                |                    |                    |                   |
                |                    |                    |                   |___return (1) + (1) [=2]
                |                    |                    |   
                |                    |                    |___fibonacci(n = 2):
                |                    |                    |                   |
                |                    |                    |                   |___fibonacci(n = 1):
                |                    |                    |                   |                   |___return 1
                |                    |                    |                   |
                |                    |                    |                   |___fibonacci(n = 0):
                |                    |                    |                   |                   |___return 0
                |                    |                    |                   |
                |                    |                    |                   |___return (1) + (0) [=1]
                |                    |                    |
                |                    |                    |___return (2) + (1) [=3]
                |                    |    
                |                    |____fibonacci(n = 3):
                |                    |                    | 
                |                    |                    |___fibonacci(n = 2):
                |                    |                    |                   |
                |                    |                    |                   |___fibonacci(n = 1):
                |                    |                    |                   |                   |___return 1
                |                    |                    |                   |
                |                    |                    |                   |___fibonacci(n = 0):
                |                    |                    |                   |                   |___return 0
                |                    |                    |                   |
                |                    |                    |                   |___return (1) + (0) [=1]
                |                    |                    |
                |                    |                    |___fibonacci(n = 1):
                |                    |                    |                   |__return 1
                |                    |                    |
                |                    |                    |___return (1) + (1) [=2]
                |                    |
                |                    |____return (3) + (2) [=5]
                |
                |____fibonacci(n = 4):
                |                    | 
                |                    |___fibonacci(n = 3):
                |                    |                   |
                |                    |                   |___fibonacci(n = 2):
                |                    |                   |                   |
                |                    |                   |                   |___fibonacci(n = 1):
                |                    |                   |                   |                   |___return 1
                |                    |                   |                   |
                |                    |                   |                   |___fibonacci(n = 0):
                |                    |                   |                   |                   |___return 0
                |                    |                   |                   |
                |                    |                   |                   |___return (1) + (0) [=1]
                |                    |                   |
                |                    |                   |___fibonacci(n = 1):
                |                    |                   |                   |___return 1
                |                    |                   |
                |                    |                   |___return (1) + (1) [=2]
                |                    |   
                |                    |___fibonacci(n = 2):
                |                    |                   |
                |                    |                   |___fibonacci(n = 1):
                |                    |                   |                   |___return 1
                |                    |                   |
                |                    |                   |___fibonacci()n = 0:
                |                    |                   |                   |___return 0
                |                    |                   |
                |                    |                   |___return (1) + (0) [=1]
                |                    | 
                |                    |___return (2) + (1) [=3]
                |
                |____return (5) + (3)
    
output:
The 6th Fibonacci number is: 8 
"""