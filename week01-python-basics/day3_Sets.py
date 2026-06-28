s = {10, 50, 20}
print(s)
print(type(s))



#2 - a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# values of a set cannot be changed
s[1] = "Hello"
print(s)



#3 - Creating an Empty Set
s = set()
print(s)
print(type(s))


#4 - Creating a Frozen Set
s = set(["a", "b", "c"])
print("Normal Set:", s)

fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)


#5 - Adding Elements to a Set
s = {"a", "b", "c"}
s.add("d")
print(s)


#6 - Union of two sets
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)


#7 - Intersection of two sets
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)



#8 - Difference of two sets
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)


#9 - Removing Elements from a Set
s = {1, 2, 3}
s.clear()
print(s)