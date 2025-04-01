#Task1 Take a list of dictionary{Name: ,age: ,citize: } check whether that person is eligible for vote or not and also check the citizen.if both conditions are True add { eligible: True}
dict={"Name":"Ramya","age":40,"citizen":"Indian"}
if dict["age"]>=18 and dict["citizen"]=="Indian":
    print("Eligible to vote")
else:
    print("Not eligible to vote")
#Task2: Take a tuple of elements, print the unique elements in the new list
tuple=(1,"hello","world",True,False,3.14,2,9.8)
strings = []
integers = []
floats = []
booleans = []
for item in tuple:
    if type(item) == str:
        strings += [item]  
    elif type(item) == int:
        if item in [True, False]:
            booleans += [item]
        else:
            integers += [item] 
    elif type(item) == float:
        floats += [item]  
print("Strings:", strings)
print("Integers:", integers)
print("Floats:", floats)
print("Booleans:", booleans)
