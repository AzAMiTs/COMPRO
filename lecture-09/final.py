try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. please enter numeric value")

finally:
    print("Excution completed, whether an exception occurred or not.")
    
print("End of program")