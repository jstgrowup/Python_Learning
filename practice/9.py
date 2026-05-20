numbers=[1, 2, 3, 4, 5]
squared=[]
for num in numbers:
    squared.append(num ** 2)

print(squared)
# Advance way
new_squared=[num **2 for num in numbers]
print(new_squared)
evens=[num for num in numbers if num%2==0]
print(evens)
odds=[num**2 for num in numbers if num%2!=0]
print(odds)
strings = ["1", "2", "3", "4", "5"]
nums=[int(new_str) for new_str in strings]
print(f"Nums: {nums}")
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
numbers_dic = [1, 2, 3, 4, 5]
squares_dict={num:num**2 for num in numbers_dic}
print(squares_dict)
