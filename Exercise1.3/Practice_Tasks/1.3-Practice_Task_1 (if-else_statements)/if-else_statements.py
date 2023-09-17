first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter addition or substraction operator: ")

if operator == '+':
    print(str(first_number + second_number))

elif operator == '-':
    print(str(first_number - second_number))

else:
    print("Unknown operator")