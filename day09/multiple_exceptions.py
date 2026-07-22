try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Number cannot be zero.")
