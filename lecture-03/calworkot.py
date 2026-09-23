hourwork = float(input("Enter the number of house worked: "))
hourrate = float(input("Enter the hourly pay rate: "))

if hourwork > 40 :
    reg_pay = 40 * hourrate
    overtime = (hourwork - 40) * hourrate * 1.5
    total = reg_pay + overtime

else:
    total = hourwork * hourrate
print(f"The gross pay is ${total:.2f}")
