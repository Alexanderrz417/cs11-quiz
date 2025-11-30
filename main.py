def add_numbers(a, b):
    return a + b 

def subtract_numbers(a, b):
    return a - b

choice = input("Do you want to do addition or subtraction? (add/subtract): ").lower()

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == "add":
    result = add_numbers(num1, num2)
    print("The result of addition is:", result)
elif choice == "subtract":
    result = subtract_numbers(num1, num2)
    print("The result of subtraction is:", result)
else:
    print("Invalid choice. Please type 'add' or 'subtract'.")
