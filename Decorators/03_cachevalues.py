# Implement a decorator that caches the return values of a function,so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
import time

def cached(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    
    return wrapper

@cached
def function1(a, b):
    time.sleep(4)
    return a + b

print(function1(2, 4))
print(function1(2, 5))
print(function1(2, 4))
print(function1(2, 5))
