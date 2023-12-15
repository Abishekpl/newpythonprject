a = int(input("enter the number "))
operator = input("enter operator ( +,-,*,/,% )")
b = int(input("enter the number "))


if operator == "+":
    print(a + b )
elif operator == "-":
    print(a - b )
elif operator == "*":
    print(a * b )
elif operator == "/":
    print(a / b )
elif operator == "%":
    print(a % b )
else :
    print("Invalid operator")
