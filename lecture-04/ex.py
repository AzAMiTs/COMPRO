cols = int(input("Enter col:"))
for i in range(1,101):
    print(i,end=" ")
    if(i%cols==0):
        print()