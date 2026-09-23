with open('sales.txt','r') as sales_file:
    lien = sales_file.readline()
    while lien != "":
        amount = float(lien)
        print(format(amount,'.2f'))
        lien = sales_file.readline()