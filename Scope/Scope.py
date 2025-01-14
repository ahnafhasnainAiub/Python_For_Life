
def calculate(num):
    def actual_func(a):
        return a ** num
    return actual_func

f = calculate(3)
g = calculate(2)

print(f(3))
print(g(3))