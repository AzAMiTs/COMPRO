print("Please select operation -")
print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
opt = int(input("Select operations form 1,2,3,4 :"))
if opt < 5:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

match opt:
    case 1:
        print(f"{num1} + {num2} = {num1+num2}")
    case 2:
        print(f"{num1} - {num2} = {num1-num2}")
    case 3:
        print(f"{num1} * {num2} = {num1*num2}")
    case 4:
        if num1 >= num2:
            print(f"{num1} / {num2} = {num1/num2}")
        else:
            print(f"{num2} / {num1} = {num2/num1}")
    case _:
        print("Unknown Status")