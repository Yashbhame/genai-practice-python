#1
print("Hello Yash")

#2
num1 = 10
print(num1)
print(type(num1))

#3
num2 = 20.5
print(num2)
print(type(num2))

#4
num3 = 30 + 2j
print(num3)
print(type(num3))

#5
name = "Yash"
print(name)
print(type(name))

#6
is_student = True
print(is_student)
print(type(is_student))

#7
a = 2
b = 3.5
print(a + b)

#8
list1 = ["English", "Maths", "Science", "History", "Geography"]
print(list1[1])
print(list1[0:3])
print(list1[-4])
print(type(list1))

#9
tuple1 = ("English", "Maths", "Science", "History", "Geography")

#10
list2 = [10, 20, 30, 40, 50]
print(list2[0]+list2[1]+list2[2]+list2[3]+list2[4])

#11
set1 = {10, 20, 30, 40, 10}   # Duplicate values are automatically removed
print(set1)

#12
list3 = ["English", "Maths", "Science", "History", "Geography"]
list3[3] = "C2W"
print(list3)

#13
dict1 = {"name": "Yash", "age": 22, "marks": 9.25}
print(dict1["name"])
print(dict1["age"])
print("marks:", dict1["marks"])
dict1["marks"] = 9.5
print(dict1["marks"])
print(type(dict1["marks"]))


#14
dict2 = {0:10, 1:20, 2:30, 3:40, 4:50}
key = 2
print(key in dict2)
'''if key in dict2:
    print("Key exists in the dictionary")
    print("Value:", dict2[key])
else:
    print("Key does not exist in the dictionary")
    '''

#15
print(dict2[2]+dict2[3])

#16
string1 = "Yash"
string2 = 'C2W'
string3 = """This is a multi-line string.
It can span multiple lines."""