
# Dictonary 
details = {"First Name": "Ahnaf", "Last Name": "Hasnain","Address": "Chittagong"}

#Print using for Loop
for all in details:
     print(all)

# Print Key with Values
# print("-----Key---&----Value----")
# for x in details:
#      print(x,":", details[x])


#Print values using .item
for key,value in details.items():
     print(key,":",value)


#Condition in dictionary
if "Address" in details:
     print("Address in Included")


# Add new values

details["Age"] = 24
print(details)

# details.pop("Age")
# details.popitem()

#Double dictionary 
vehicle = {
     "Car": {"BMW": "Germany", "Toyota": "Japan", "Hyundai": "South Korea", "Porshe": "Italy"},
     "Bike": {"Suzuki":"Japan", "Runner":"Bangladesh", "Bajaj": "India"} 
}

print(vehicle["Bike"]["Suzuki"])

# Squared Number 
sqr_number ={ n:n**2 for n in range(5)}
print(sqr_number)

#Type
print(type(sqr_number))