num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
if num1 > num2:
    if num1 > num3:
        large = num1
    else:
        large = num3
else:
    if num2 > num3:
        large = num2

    else:
        large = num3

print("The biggest of",num1, num2, num3, "is",large)

