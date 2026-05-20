### **Technical Notes: Python Data Types - The Big Picture**

This video provides a foundational overview of Python's data types, also referred to as **Object Types**, emphasizing that in Python, almost everything is treated as an object.

---

### **1. Numbers**

Python supports various types of numerical data and high-precision calculations.

- **Integers and Floats:** Includes standard whole numbers (1, 2, 3) and decimal values (3.14).
- **Complex Numbers:** Supports numbers with a real and imaginary part, such as `3 + 4j`.
- **Special Types:** Includes `Decimal` and `Fraction` for specific mathematical requirements.
- **Power Operations:** Use the double asterisk `**` for calculating powers.

```python
# Basic Math
print(12 + 12)    # Returns 24
print(2 ** 4)     # 2 to the power of 4 (16)
print(2 ** 100)   # Python supports very large numbers
```

---

### **2. Strings**

Strings are sequences of characters used to store text. In Python, they are **immutable**, meaning they cannot be changed in place once created.

- **Syntax:** Can be enclosed in single (`'...'`) or double (`"..."`) quotes.
- **Indexing & Slicing:** Strings can be indexed (starting at 0) or sliced to extract portions.
- **Negative Indexing:** Using `-1` accesses the last character of the string.

```python
username = "chai aur code"

# Indexing
print(username)    # Returns 'c'
print(username[-1])   # Returns 'e' (last character)

# Slicing (Start : End - End is not included)
print(username[1:3])  # Returns 'ha'

# Immutability Check (This will raise a TypeError)
# username = 'A'
```

---

### **3. Lists**

Lists are continuous memory spaces that store a collection of items. They are **mutable** and can hold different data types simultaneously.

- **Heterogeneous:** A single list can contain integers, strings, floats, and even other lists.
- **Indexing:** Like strings, lists are zero-indexed.

```python
my_list = [123, "chai", 3.14]
print(len(my_list))  # Returns 3 (Human-readable length)
print(my_list)    # Returns 123
```

---

### **4. Dictionaries (Dict)**

Dictionaries store data in **key-value pairs** using curly braces `{}`. Unlike lists, they are not accessed by numerical index but by their unique keys.

- **Custom Keys:** You can define your own indices (keys) as strings or numbers.

```python
my_d = {
    "one": "lemon tea",
    "two": "ginger tea",
    "comic": "nagraj"
}

print(my_d["comic"])  # Returns 'nagraj'
# Accessing a non-existent key results in a 'KeyError'
```

---

### **5. Tuples and Sets**

- **Tuples:** Similar to lists but defined with parentheses `()`. They are often used for fixed data collections.
- **Sets:** Defined using curly braces but contain only **unique values**; duplicates are automatically removed.

---

### **6. Boolean and None**

- **Boolean:** Represents logical values: `True` or `False`.
- **None:** A special type representing "nothing" or an empty reference. It is useful when an operation (like an API call) returns no data.

---

### **7. Using Built-in Modules**

Python provides powerful built-in libraries like `math` and `random` to extend functionality.

```python
import math
print(math.pi)    # Returns 3.14159...

import random
print(random.random())           # Returns a random float
print(random.choice())  # Returns a random item from the list
```

---

### **8. Advanced Concepts Overview**

The video sets the stage for future in-depth discussions on:

- **Functions, Modules, and Classes:** The building blocks of structured programming.
- **Decorators and Generators:** Tools to enhance existing functions and handle data streams.
- **Meta-programming:** Advanced logic for modifying code behavior.
