try:
    a= int(input("n$%"))
    print(a)
except ValueError:
    print("Invalid input through keyboard")
finally:
    print("Program has ended")