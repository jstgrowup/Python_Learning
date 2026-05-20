# def keyword — Defines a function
# Parameters — Variables the function accepts (no type declarations needed)
# Docstring (optional) — Description in triple quotes """
# Indentation — Everything inside the function must be indented
# return — Sends a value back to the caller

# def greet(name):
#     message=f"Helo,{name}"
#     return message
# result=greet("subham")
# print(result)
from datetime import date
def calculate_age(birth_year):
    current_year=date.today().year
    current_age=current_year-birth_year
    return current_age
age=calculate_age(1999)
print(age)