# count = 0
# while count < 5:
#     print("hello : ",count)
#     count +=1


keep_going = 'y'

while keep_going == 'y':
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    commission = sales * comm_rate

    print(f'the commission is ${commission:.2f}')

    keep_going.lower = input("do you want to calculate anoter" + \
                       'commission (Enter y for yes): ')