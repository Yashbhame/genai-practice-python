#1-basic if-else statement
'''
age = 20
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
'''

#2 - if-elif-else statement
'''
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
'''

#3 - nested if else statement
'''
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Eligible to drive.")
    else:
        print("Need a driver's license.")
else:
    print("Not old enough to drive.")
'''

#4 Ternary operator (conditional expression)
'''
age = 20
result = "Eligible to vote." if age >= 18 else "Not eligible to vote."
print(result)
'''

#5 match case statement
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")