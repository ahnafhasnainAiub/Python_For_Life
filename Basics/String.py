name = "Ahnaf Hasnain Nahiun"
slice_name = name[0:5]
slice_name2 =  name[-2]
slice_name3 = name[0:13:3]

print(slice_name3)


# Using Strip Method For No Space
x = "      hello everyone    "
print(x)
print(x.strip().upper())


# Using Split
dept = "BBA, CSE, EEE, LLB, Arch"
print(dept)
print(dept.split(", "))

# using Replace()
print(dept.replace("LLB","ME"))