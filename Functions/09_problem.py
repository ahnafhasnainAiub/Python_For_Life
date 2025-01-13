# Write a generator function that yeilds even numbers up to a specified limit.

# yield key word use for store in memory and then return the value when need

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)