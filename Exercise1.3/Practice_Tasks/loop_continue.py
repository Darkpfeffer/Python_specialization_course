num = int(input("Enter a number to be divided: "))
start = int(input("Enter a starting point for the divisor: "))
end = int(input("Enter an end point for the divisor: "))

for div in range(start, end):
    if div == 0:
        print("Division by zero, skipping to the next value.")
        continue
    print(num / div)