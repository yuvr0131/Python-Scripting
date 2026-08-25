#Writing appending files
# employee_file=open("emplyee.txt","r")
employee_file=open("emplyee.txt","a")
employee_file.write("TOBBY - Human Resources")
# print(employee_file.read())
employee_file=open("emplyee.txt","w")
employee_file.write("\n Kelly - Customer Service")
employee_file.close()