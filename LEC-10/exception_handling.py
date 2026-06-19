try:
    num = int(input("Enter a Number ="))
    result = 10/num 
    print("Result :", result)

except ZeroDivisionError:
    print("You cannot divide wih zero")
