with open('sales.txt','r') as sales_file:
    for line in sales_file:
        amout = float(line)
        print(format(amout,'.2f'))