# A dictionary stores data as key-value pairs. It's essentially a Python object, just like a JavaScript object!
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# age=person["age"]
# print(age)
# del person["age"]
# print(person)
# keys=person.keys()
# print(keys)
# values=person.values()
# print(values)
# for key in person:
#     print(key)
# for key,value in person.items():
#     print(f"{key}: {value}")
# for value in person.values():
#     print(value)


movie={
   "title":"Inception",
   "director":"Christopher Nolan",
   "year":2010,
   "rating":8.8
}
print(movie["title"])
movie["genre"]="Sci-fi"
for key,value in movie.items():
    print(f"{key}: {value}")