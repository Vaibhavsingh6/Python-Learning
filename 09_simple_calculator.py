num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

operator = input("Enter a operator(+,-.*,/):")

if operator == "+":
    result = num1+num2
    print("result",result)

elif operator == "-":
    result = num1 - num2
    print("result",result)

elif operator == "*": 
    result = num1*num2
    print("result",result)

elif operator == "/":
    result = num1/num2
    print("result",result)

else:
    print("Invaild Operators")
