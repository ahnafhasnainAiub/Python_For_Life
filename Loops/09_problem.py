# Check if all elements in a list are unique .if a duplicate is found, exit the loop and print the duplicate.

items = ["Ahnaf","Hasnain","Nahiun","Elham","Nahiun"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item is ",item)
        break
    unique_item.add(item)
