employee_file=open("emplyee.txt","r")
# print(employee_file.readable())
# print(employee_file.read()) # to read the entire content in files
# print(employee_file.readline()) # to read individual lines
# print(employee_file.readlines()) # puts the entire content of file in an array

# using for loop
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
