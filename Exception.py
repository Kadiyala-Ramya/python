#1Using only try--The try block lets you test a block of code for errors.

#2Using try and except
try:
    print("10k Coders")
except:
    print("error")

#3--Since the try block raises an error, the except block will be executed.
try:
    print(10/0)
except ZeroDivisionError:
    print("A number can't divisible by zero")

#4
try:
    print(x)
except ZeroDivisionError:
    print("A number can't divisible by zero")
except:
    print("Something is wrong")

#5--#The try block does not raise any errors, so the else block is executed.Otherwise only except block executes.
try:
    print(10/0)
except:
    print("Something is wrong")
else:
    print("Life is very short, just live it")

#6--The finally block executed even if the try block executes an error or not
try:
    print("Welcome to the World")
except:
    print("Something is wrong")
else:
    print("Life is very short, just live it")
finally:
    print("Thank you")

#7
try:
    print(x)
except ZeroDivisionError:
    print("A number can't divisible by zero")
except:
    print("Something is wrong")
finally:
    print("Error")

#8
try:
    x=5
    y=3
    z=x+y
    print(z)
    try:
        print(a)
    except:
        print("Error found")
except:
    print("Something is missing")





#Removes letter from string using index
def remove(s, i):
    return s[:i]+s[i+1:]
print(remove("hello",3))

#formatting string
a=3.1456
b=-12.4678
c=+5.678
print(f"{a:.2f}")
print(f"{b:+.2f}")
print(f"{c:+.2f}")
x = 25
print(f"x is {x}")
a=25
b=12
print(f"the addition of a and b is {a+b}")
