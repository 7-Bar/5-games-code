first_number = float(input("Enter the first number: "))
operation = input("Enter the operation: ")
second_number = float(input("Enter the second number: "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number
else:
    print("invaild operation")
    quit()

print(f"{first_number} {operation} {second_number} = {result}")