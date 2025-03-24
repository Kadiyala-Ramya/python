#Task:1 Practice all Methods
print("String methods")
a="coders"
b=a.upper()
print(b)
c="CODERS"
d=c.lower()
print(d)
e="I like guava"
f=e.replace("guava","apple")
print(f)
g="we,are,devlopers"
h=g.split(",")
print(h)
k='  "we" are devlopers'
i=k.lstrip()
print(i)
l='we are "devlopers"   '
j=l.rstrip()
print(j)
m=l.startswith("we")
print(m)
n=l.endswith("pers")
print(n)
o=l.find("are")
print(o)
p=l.count("e")
print(p)
q=l.title()
print(q)
r=l.capitalize()
print(r)

#Task2 Take a string it contains both upper and lower case ,print the no of vowels and consonants present in the string
print("Take a string it contains both upper and lower case ,print the no of vowels and consonants present in the string")
str="constitution"
vowels=0
consonants=0
for i in range(0,len(str)):
    char=str[i]
    if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        vowels+=1
    else:
        consonants+=1
print("Vowels:",vowels)
print("consonants:",consonants)