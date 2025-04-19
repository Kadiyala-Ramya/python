#Research more about scopes and applications. And try to solve problems
#A variable is only available from inside the region it is created. This is called scope.
#Local scope: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def func():
    x=100
    print(x)
func()        #output: 100


def func():
    x=100
    print(x)
func()     
print(x)        #output:100 error x is not defined


def outerfunc():
    def innerfunc():
        x=300
    innerfunc()
    print(x)
outerfunc()       #output: error x is not defined


#Global scope: A variable created in the main body of the Python code is a global variable and belongs to the global scope.
x=100
def func():
    print(x)
func()
print(x)         #output: 100 100


x=100
def func():
    x=300
    print(x)
func()
print(x)         #output: 300 100


#using global keyword
def func():
    global x
    x=100
func()
print(x)        #output: 100


x=100
def func():
    global x
    x=300
func()
print(x)      #output: 300


x=100
def func():
    global x
    print(x)
    x=300
    print(x)
func()
print(x)       #output: 100 300 300


#Nonlocal keyword
def func():
    x=100
    def innerfunc():
        nonlocal x
        x=300
    innerfunc()
    print(x)
func()              #output: 300


def func():    #without nonlocal keyword
    x=100
    def innerfunc():
        x=300
    innerfunc()
    print(x)
func()              #output: 100
  