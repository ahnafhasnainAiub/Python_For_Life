file = open('filemanager.txt', 'w')

try:
    file.write("Ahnaf Hasnain")
finally:
    file.close()


with open('TaskManager.txt', 'w') as file:
    file.write('Mr. Ahnaf Hasnain Nahiun')