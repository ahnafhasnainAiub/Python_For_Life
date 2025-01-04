# Keep asking the user for input untill they enter a number between 1 and 10.

while True:
    number = int(input("Enter Valid Number : "))
    if 1<= number <=10:
        print("Thanks")
        break
    else:
        print("Number is Invalid")