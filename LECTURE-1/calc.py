import math

print("===== Scientific Calculator =====")

while True:
    print("\nOperations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log10")
    print("11. Natural Log (ln)")
    print("12. Factorial")
    print("13. Value of Pi")
    print("14. Value of e")
    print("15. Exit")

    choice = int(input("\nEnter your choice (1-15): "))

    if choice == 15:
        print("Calculator Closed.")
        break

    if choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", a + b)

        elif choice == 2:
            print("Result =", a - b)

        elif choice == 3:
            print("Result =", a * b)

        elif choice == 4:
            if b == 0:
                print("Division by zero is not allowed!")
            else:
                print("Result =", a / b)

        elif choice == 5:
            print("Result =", a ** b)

    elif choice == 6:
        num = float(input("Enter number: "))
        print("Result =", math.sqrt(num))

    elif choice == 7:
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.sin(math.radians(angle)))

    elif choice == 8:
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.cos(math.radians(angle)))

    elif choice == 9:
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.tan(math.radians(angle)))

    elif choice == 10:
        num = float(input("Enter number: "))
        print("Result =", math.log10(num))

    elif choice == 11:
        num = float(input("Enter number: "))
        print("Result =", math.log(num))

    elif choice == 12:
        num = int(input("Enter integer: "))
        print("Result =", math.factorial(num))

    elif choice == 13:
        print("Pi =", math.pi)

    elif choice == 14:
        print("e =", math.e)

    else:
        print("Invalid Choice!")