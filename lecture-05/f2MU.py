def calcurate_state(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximun = max(numbers)
    minimun = min(numbers)
    return total_sum,average,maximun,minimun

numbers = [5,10,15,20,25]
total,avg,max_num, min_num = calcurate_state(numbers)

print(f"Total sum: {total}")
print(f"average: {avg}")
print(f"Maximun: {max_num}")
print(f"Minimum {min_num}")