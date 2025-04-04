print("Set Methods:")
a={'a','b','c'}
a.add('d')
print(a)
b={1,2,3,4}
b.clear()
print(b)
c={'A','B','C'}
d=c.copy()
print(d)
e={'a','b','c','d'}
f={'a','b'}
g=e.difference(f)
print(g)
h={'a','b','c'}
h.discard('c')
print(h)
i={'a','b','c','d'}
j={'a','b'}
k=i.intersection(j)
print(k)
k=i.symmetric_difference(j)
print(k)
l={'a','b','c','d'}
m={'e','f'}
n=l.isdisjoint(m)
print(n)
o={'a','b','c','d'}
p={'a','b'}
q=p.issubset(o)
print(q)
r=o.issuperset(p)
print(r)
s=o.union(p)
print(s)
o.pop()
print(o)
print("Frozenset Methods:")
A=frozenset([2,5,7,8])
B=frozenset([8,9,5,3])
C=A.copy()
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
D=frozenset([2,5])
print(A.isdisjoint(B))
print(D.issubset(A))
print(A.issuperset(D))

#Take a set of no,take elements from user remove that element from existing set and store in new set
print("Take a set of no,take elements from user remove that element from existing set and store in new set")
E={'a','b','c','d'}
F=set()
U=input("Enter your elements to remove:")
for i in U.split(","):
        if i in E:
            E.remove(i)
            F.add(i)
print("Existing set:",E)
print("New set:",F)
