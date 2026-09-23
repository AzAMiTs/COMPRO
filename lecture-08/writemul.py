import struct

num_rec = int(input("How many rec "))
with open('recodes.bin','wb') as file:
    for _ in range(num_rec):
        id_num = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gpa = float(input("Enter GPA: "))
        
        data =struct.pack('i20sif',id_num,name.encode('utf-8'),age,gpa)
        
        file.write(data)
print(f"{num_rec} record have been written to records bin")