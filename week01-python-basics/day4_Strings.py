#1
a = 'Yash'  
b = "Yash Bhame here" 
c = """
This is a multi line string
hello there
""" 
print(a)
print(b)


print(a[3])
print(a[-2])
print(b[2:5])

for char in c:
    print(char)


#2 strings immutability
s = "aBCDEF"
s = "A" + s[1:]  #new string gets created
print(s)

#3
s = "Hellothere"
print(len(s))


#4
s = "Hello World"
print(s.upper())
print(s.lower())

#5
s = "   ABC   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))

#6
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)