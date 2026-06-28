#1 - creating a basic tuple
t = (1, 2, 3, 4, 5)
print(t)
print(type(t))


#2 - creating a tuple with mixed datatypes
tup = (1, "Hello", 3.4)
print(tup)


#3 - Accessing Elements of a Tuple
tup = tuple("hello")
print(tup[0])
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("hello", "For", "world")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)



#4 - Concatenating Tuples
tup1 = (0, 1, 2, 3)
tup2 = ('hello', 'For', 'world')
tup3 = tup1 + tup2
print(tup3)


#5 - Slicing Tuples
tup = tuple('ALLTHEBEST')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])


#6 - Deleting Tuples
'''
tup1 = (0, 1, 2, 3, 4)
del tup1
print(tup1)
'''