# COS202 Mathematical Calculator

import math

print("=================================")
print("     MATHEMATICAL CALCULATOR")
print("=================================")

while True:
    print("\nChoose an operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Power (^)")
    print("7. Percentage (%)")
    print("8. Modulus (Mod)")
    print("9. Clear Screen")
    print("10. OFF")

    choice = input("\nEnter your choice (1-10): ")

    if choice == "10":
        print("Calculator is OFF.")
        break

    elif choice == "9":
        print("\n" * 50)
        continue

    elif choice == "5":
        num = float(input("Enter a number: "))
        print("Answer =", math.sqrt(num))

    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", num1 + num2)

        elif choice == "2":
            print("Answer =", num1 - num2)

        elif choice == "3":
            print("Answer =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Answer =", num1 / num2)
            else:
                print("Division by zero is not allowed.")

        elif choice == "6":
            print("Answer =", num1 ** num2)

        elif choice == "7":
            print("Percentage =", (num1 / num2) * 100, "%")

        elif choice == "8":
            print("Answer =", num1 % num2)

        else:
            print("Invalid choice. Try again.")
