a=int(input("Enter a number"))
b=int(input("Enter another number"))
try:
    c=a / b
    print(c)
except ZeroDivisionError:
    print("cannot divide by zero")