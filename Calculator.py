def add(x, y):
    return x + y



def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def mul(x, y):
    return x * y

def sub(x, y):
    return x - y        


num1 = float(input("Enter  first number: "))
num2 = float(input("Enter second number: "))


print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice = input("Enter choice (1/2/3/4): ")


if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = sub(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = mul(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    result = div(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print(" Please enter a valid choice (1/2/3/4).")

