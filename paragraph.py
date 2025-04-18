#Take a string with a paragraph ..
#Print valid if that string contains only alphabets and spaces
#If not print invalid Without using direct methodsA


s="An apple a day keeps a doctor away"
valid = True
for i in s:
    if not ((65<=ord(i)<=90) or (97<=ord(i)<=122) or (ord(i)==32)):
        valid = False
        break
if valid:
    print("valid")
else:
    print("invalid")
    