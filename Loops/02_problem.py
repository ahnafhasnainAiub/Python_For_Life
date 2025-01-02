# Calculate the sum of Even Numbers up to a given numbers n.and
  
n = 100
total_even = 0
for i in range(1, n+1):
    if i % 2 == 0:
        total_even += 1
print("Sum of Even Numbers in N Numbers : ",total_even)