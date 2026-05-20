# age =int (input("Enter your age:  "))
try:
    age =int (input("Enter your age:  "))
except :
    print("Not a valid number")
finally:
    print("In Finally")
# ValueError - wrong type/value
try:
    age = int("abc")  # Can't convert "abc" to int
except ValueError:
    print("Invalid number!")

# KeyError - dictionary key doesn't exist
try:
    person = {"name": "Alice"}
    print(person["age"])  # Key doesn't exist!
except KeyError:
    print("That key doesn't exist!")

# IndexError - list index out of range
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # Index 10 doesn't exist!
except IndexError:
    print("That index doesn't exist!")

# FileNotFoundError - file doesn't exist
try:
    with open("nonexistent.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")