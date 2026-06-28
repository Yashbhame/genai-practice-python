
#1 - Creating a Dictionary
a = {"x": 1, "y": 2}
print(a)

b = dict(name="Sam", age=20)
print(b)



#2 - Accessing Dictionary Elements
d = {"name": "Kat", "age": 21}

print(d["name"])     # Access using key
print(d.get("age"))  # Access using get()


#3 - Adding and Updating Dictionary Elements
d = {"name": "Sam"}

d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)



#4 - Deleting Dictionary Elements
d = {"a": 1, "b": 2}
del d["a"]
print(d)


#5 - Dictionary Methods
d = {"a": 1, "b": 2}

val = d.pop("a")
print(val)
print(d)


#6 - Dictionary Methods
d = {"a": 1, "b": 2}
print(d.popitem())



#7 - Dictionary Methods
d = {"a": 1, "b": 2}
d.clear()
print(d)


#8 - Iterating through a Dictionary
d = {"a": 1, "b": 2}
for key in d:
    print(key)


#9 - Iterating through a Dictionary
d = {"a": 1, "b": 2}
for value in d.values():
    print(value)


#10 - Iterating through a Dictionary
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)



#11 - Nested Dictionaries
d = {
    "student": {
        "name": "Sam",
        "age": 20
    }
}

print(d["student"]["name"])