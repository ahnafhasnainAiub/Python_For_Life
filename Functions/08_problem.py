# Write a function that takes variable number of arguments and returns their sum.

def kw_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kw_args(name="Ahnaf Hasnain", age=25, degree="BSc in Cse")
kw_args(height="5'7", weight=71)