age = int(input("How old are you? "))
if age < 18:
    print("You are a minor.")  
else:    print("You are an adult.")
if age >= 65:
    print("You are a senior citizen.")


print("\nLet's do some math!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation"

print("Result:", result)