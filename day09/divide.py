try:
    a = int(input("First number: "))
    b = int(input("Second number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("You cannot divide by zero.")
