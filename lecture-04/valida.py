score = int(input("Enter a test score: "))

while score < 0 or score > 100 :
    print("error: the score cannot be negative")
    print("or greater than 100.")


    score = int(input("enter the correct scoe:"))