#1 - for loop 

n = 4
for i in range(0, n):
    print(i)


a = ["hello", "for", "practice"]
for idx in range(len(a)):
    print(a[idx])


#2 - while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello There")


#3 - nested for loop
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


#4 break statement
num = int(input("Enter a number: "))
x = 1
while x <= num:
    if x == 5:
        break
    print(x)
    x = x + 1

#5 continue statement
num = int(input("Enter a number: "))
x = 1
while x <= num:
    if x == 5:
        x = x + 1
        continue
    print(x)
    x = x + 1


#6 pass statement
for i in range(1, 6):
    if i == 3:
        pass 
    else:
        print(i)

#7 while else statement
count = 0
while count < 3:
    count = count + 1
    print("Hello There")
else:
    print("Loop finished.")


#8 for else statement
data = [2,4,6,8,10]
for i in data:
    if i % 3 == 0:
        break
    print(i)
else:
    print("in else block")

#9 range function
for i in range(0,5,2):
    print(i)

#10 nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j = j + 1
    i = i + 1


#11 nested for loop 
for i in range(3):
    for j in range(2):
        print("hello")