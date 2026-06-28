#1 - creating a basic list
a = [1, 2, 3]
print(a)

b = ["apple", "banana"]
print(b)


#2 - creating a list using the list() constructor
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("GFG")
print(b)



#3 - creating a list with repeated elements
a = [2] * 5
b = [0] * 7

print(a)
print(b)



#4 - Accessing List Elements
a = [10, 20, 30]
print(a[0])
print(a[-1])



#5 adding elements to a list
a = [1, 2]
a.append(3)
print(a)


#6 - adding using insert()
a = [1, 3]
a.insert(1, 2)
print(a)


#7 - adding using extend()
a = [1, 2]
a.extend([3, 4])
print(a)


#8 - updating list elements
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)


#9 - removing elements from a list
a = [1, 2, 3]
a.remove(2)
print(a)

#10 - removing elements using pop()
a = [1, 2, 3]
a.pop()
print(a)

#11 - removing elements using del
a = [1, 2, 3]
del a[1]
print(a)


#12 - removing elements using clear()
a = [1, 2, 3]
a.clear()
print(a)


#13 - iterating through a list
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)



#14 - nested lists
a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0])