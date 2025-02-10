def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

# Example usage
if __name__ == "__main__":
    number = 5
    print(f"The sum of all integers from {number} to 1 is: {recursive_sum(number)}")

"""
explanation:
function call for n = 5:

    function call for n = 4:
    
        function call for n = 3:
        
            function call for n = 2:
                
                function call for n = 1:
                    return 1
                    
                return 2 + (1)
            
            return 3 + (2 + 1)
            
        return 4 + (3 + 2 + 1)
    
    return 5 + (4 + 3 + 2 + 1)

output:
The sum of all integers from 5 to 1 is: 15                
"""