# str="Subham Dey"
# print(str.upper())
# print(str.lower())
# print(str.replace("u","w"))
# print(str.split(" "))
# print(str.strip())
# print(str.startswith("s"))
# sentence = " ".join(["Hello", "from", "Python"])
# print(sentence)
# print(str.endswith("y"))
# print(str.count("e"))
# print(sentence[2:5])

user_input = input("Please enter the full Name: ")

# Strip whitespace and convert to title case
user_input = user_input.strip()
user_input = user_input.title()
print(f"Your name: {user_input}")

# Count letters without spaces
name_length = len(user_input.replace(" ", ""))
print(f"Name length (no spaces): {name_length}")

# Check if contains letter 'a' (case-insensitive)
contains_a = "a" in user_input.lower()
print(f"Contains 'a': {contains_a}")