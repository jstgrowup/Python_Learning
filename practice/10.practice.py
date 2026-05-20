try:
    num_1 = int(input("Enter a Number: "))
    num_2 = int(input("Enter the second number: "))
    division = num_1 / num_2
    print(f"Result: {division}")
except ValueError:
    print("Error: Please enter valid numbers!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("Operation Completed")
