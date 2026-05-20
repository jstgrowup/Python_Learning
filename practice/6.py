# A list is an ordered collection of items
# fruits=["apple","banana","orange"]
# numbers=[1,2,3,4,5]
# mixed=["Alice",21,True,3.43]
# # Python uses len() instead of .length property!
# print(len(fruits))
# mixed.append(4343)

# # Methods
# numbers.sort()
# numbers.reverse()
# numbers.count(1)  #Count occurences
# numbers.index(3)
# numbers.insert(0,0)


student_scores=[85, 92, 78, 95, 88]
maximum=max(student_scores)
print(f"maxiumum: {maximum}")
minimum=min(student_scores)
print(f"minimum: {minimum}")

average=sum(student_scores)/len(student_scores)
print(f"average: {average}")
