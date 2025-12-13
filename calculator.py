calculator = input("Enter the operation you want to perform: (+, -, *, /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if calculator == "+":
    print (a+b)

elif calculator == "-":
    print (a-b)

elif calculator == "*":
    print (a*b)

else:
    print (round (a/b, 2))









