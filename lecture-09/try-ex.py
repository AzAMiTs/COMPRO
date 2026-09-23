try:
    x = 10 / 0
    print(x)
except ZeroDivisionError as e:
    print(f"Error: {e}")

print("End of program")
