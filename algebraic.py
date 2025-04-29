#Write a program to print the string aaabbc as a3b2c1?
s="aaabbc"
n=s[0]
c=0
res=" "
i=0
while i<len(s):
    if s[i]==n:
        c+=1
    else:
        res += n + str(c)
        n = s[i]
        c = 1
    i+=1
res += n + str(c)
print(res)



#Shallow copy--Changes to nested objects in one affect the other.
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print(original)  #[[99,2],[3,4]] → changed


#Deep copy--Changes in one do not affect the other.
deep = copy.deepcopy(original)
deep[0][0] = 100
print(original)  # [[99, 2], [3, 4]] → unchanged


#Decorator:A decorator is a function that takes another function as input and extends or modifies its behavior without changing its source code.
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")
say_hello()


#Memory allocation:--Python automatically manages memory using a private heap. All objects are stored in this heap, and memory is allocated dynamically.
