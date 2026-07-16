operater = input("Enter a operater that you need (+ - * /)")
num1 = float(input("Enter the 1st number "))
num2 = float(input("Enter the 2nd number "))

if operater == "+":
    print(num1 + num2)
elif operater == "-":
    print(num1 - num2)
elif operater == "*":
    print(num1 * num2)
else:
    print(num1 / num2)