python# Simple Calculator Application
# Git & GitHub Capstone Project
# Developer2 Branch: Added modulus operation

def add(a, b):
    result = a + b
    print(f"Addition: {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    print(f"Subtraction: {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    print(f"Multiplication: {a} x {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    result = a / b
    print(f"Division: {a} / {b} = {result}")
    return result

def modulus(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    result = a % b
    print(f"Modulus: {a} % {b} = {result}")
    return result

def calculator_menu():
    print("=" * 40)
    print("  Welcome to Simple Calculator App - Updated by Developer2")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    print("=" * 40)
    while True:
        calculator_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '6':
            print("Thank you!")
            break
        if choice in ['1','2','3','4','5']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == '1': add(a, b)
            elif choice == '2': subtract(a, b)
            elif choice == '3': multiply(a, b)
            elif choice == '4': divide(a, b)
            elif choice == '5': modulus(a, b)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    calculator_menu()