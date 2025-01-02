# Problem -  Given a string, find the first Non-Repeated character

input_str = "ahhnaff"

for char in input_str:
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break