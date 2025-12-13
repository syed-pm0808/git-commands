a = 10
b = int(input("Enter a number: "))
try:
    c = a/b
    #c = round(c)
    print(c)
except:
    print("You can't divide by zero!")
    #print(round(c, 2))