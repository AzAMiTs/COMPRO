keep_go = 'y'

while keep_go == 'y':
    wholesale = float(input("enter the item's wholesale cost:"))
    retail_price = wholesale * 2.5

    print(f'retail_price: ${retail_price:.2f}')
    
    gekey = input("have anoter")
    keep_go = gekey.lower()