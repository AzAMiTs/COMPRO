with open('employee.txt','r') as emp_file:
    line = emp_file.readline()
    while line != "":
        name = line.strip()
        id_num = emp_file.readline().strip()
        dept = emp_file.readline().strip()
        
        print("Name:",name)
        print("ID:",id_num)
        print("Department:",dept)
        
        line = emp_file.readline()