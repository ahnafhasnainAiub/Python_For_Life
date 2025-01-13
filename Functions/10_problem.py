# Create a Recursive function to calculate the factorial of a number

# In recursion always think first about exit!!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))