def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
print("Welcome to Unique Calculator!")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice: str = input("Enter choice (1/2/3/4): ")
if choice not in ['1', '2', '3', '4']:
    print("Invalid choice")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        result = add(num1, num2)
        operation = "+"
    elif choice == '2':
        result: float = subtract(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "*"
    else:
        result = divide(num1, num2)
        operation = "/"
    print(f"{num1} {operation} {num2} = {result}")
