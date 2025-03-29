print("Regular functions")
def hello():
    print("Hello, Welcome to the World!")
hello()
print("Default parameters")
def greet(name="User",greeting="Hai"):
    print(f"{greeting}, {name}!")
greet() 
greet("Ramya")
greet("Ramya","hi")
print("Keyword Arguments")
def function(name, age):
      print("My name is"+name)
      print("My age is"+age)
function(age=24, name="Ramya")
function(name="Ramya", age=24)
print("Positional Arguments")
def function(name, age):
      print("My name is"+name)
      print("My age is"+age)
function(24, "Ramya")
function("Ramya", 24)
print("Arbitrary Arguments")
def function(*numbers):
     return sum(numbers)
print(function(1,2,3,4,5))
def function(**kwargs):
   for key, value in kwargs.items():
        print(f"{key}: {value}")
function(name="Ramya", age=24, city="Ongole")
print("Resursive Functions")
def evenOdd(n):
     if n%2==0:
          print("Even number")
     else:
          print("Odd number")
evenOdd(4)
evenOdd(7)
print("Lambda Functions")
addition=lambda x,y:x+y
print(addition(2,5))


