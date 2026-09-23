weight = float(input('Enter weight in kilograms: '))
height = float(input('Enter height in meters(1 = 100cm): '))

bmi = weight / (height * height)
# bmi = weight / ((height/100) * (height/100))

print('Your BMI is',format(bmi,'.2f'))