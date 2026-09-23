age = int(input("Enter you age: "))
income = int(input("Enter you salary: "))

if age >= 18 and age <= 65 and income > 30000:
    print('You are eligivle for the loan')
else:
    print('You are not eligible for the loan')
