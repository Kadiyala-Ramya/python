import random as r
print("Random float between 0 and 1: ",r.random())
print("Random integer between 1 and 10: ",r.randint(1,10))
print("Random range between 1 and 10: ",r.randrange(1,10,2))
items=['a','b','c',1,2,3]
print("Random choice from list",r.choice(items))
print("Random choice from list",r.choices(items,k=2))
print("List of random elements with repetition: ",r.sample(items,k=3))
l=[2,3,1,4]
r.shuffle(l)
print(l)
print("Random float: ",r.uniform(1.5,2.5))
