num_emp = 6

def mian():
    hours = [0] * num_emp
    
    for index in range(num_emp):
        print("Enter the hour worked by employee", \
            index + 1,": ",sep="",end='')
        hours[index] = float(input())
        
    pay_rate = float(input("Enter the horly"))
    
    for index in range(num_emp):
        gross_pay = hours[index] * pay_rate
        print("Gross pay for emp",index + 1, ": $",\
            format(gross_pay,',.2f'),sep='')
        
        
        
mian()