# Compute the factorial of a number using a while loop

numb = 5
factorial = 1

while(numb > 0):
    factorial *= numb
    numb -= 1
    
print("Factorial is :", factorial)