employee_file = open("employee.txt","a")#if we write "w" instead of "a" then it will override all content of the file 
employee_file = open("employee1.txt","w")#this will create a new file
employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")

employee_file = open("index.html","w")
employee_file.write("<p>This is HTML</p>")