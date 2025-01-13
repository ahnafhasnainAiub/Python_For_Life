# Write a function that takes variable number of arguments and returns their sum.

def diff_sum(*args):
    return sum(args)

print(diff_sum(2,3))
print(diff_sum(5,4,1))
print(diff_sum(4,5,2,8,2))