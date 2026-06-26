#1-basic function
def fun1():
    print("Welcome to function 1")

fun1()


#2-evenodd function(a function to check even odd values)
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))


#3-function with default argument
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

#4 keyword arguments
def student(fname, lname):
    print(fname, lname)

student(fname='Ash', lname='Born')
student(lname='Kaiser', fname='John')

#5 Positional arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Ronaldo", 41)

print("Case-2:")
nameAge(41, "Ronaldo")  # This will cause an error because the order of arguments is incorrect.


#6 Arbitrary arguments (*args, **kwargs)
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='FIFA', mid='final', last='Games')

#7 Function inside function
def outerFun():
    print("This is the outer function.")

    def innerFun():
        print("This is the inner function.")

    innerFun()

outerFun()

#8 return statement
def sq_value(num):
    return num**2

print(sq_value(2))
print(sq_value(-4))