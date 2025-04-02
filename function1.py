#perform basic mathematical operations (+,-,,/,//,%,*) using def function and lambda functions
print("Using def functions")
def add(a, b):
    return a + b

def subtract(a, b):
    return a -b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
       return a / b 
    else:
       return "Cannot divide by zero"

def floor_divide(a, b):
    if b != 0:
        return a // b 
    else:
        return "Cannot divide by zero"

def modulus(x, y):
    return x % y
print(add(10, 5))        
print(subtract(10, 5))   
print(multiply(10, 5))   
print(divide(10, 0))     
print(floor_divide(10, 3)) 
print(modulus(10, 3))    

print("Using Lambda functions")
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"
floor_divide = lambda x, y: x // y if y != 0 else "Cannot divide by zero"
modulus = lambda x, y: x % y
print(add(10, 5))        
print(subtract(10, 5))   
print(multiply(10, 5))   
print(divide(10, 0))     
print(floor_divide(10, 3)) 
print(modulus(10, 3))    
.