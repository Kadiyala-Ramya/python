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