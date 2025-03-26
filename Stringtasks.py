#Task 1: Take a paragraph check the count of words, if count is more than 100, print valid ; else invalid
print("Take a paragraph check the count of words, if count is more than 100, print valid ; else invalid")
para = input("Enter your paragraph:")
p=len(para.split())
if p>100:
    print("valid")
else:
    print("invalid")
#Task2: take a input with both upper and lower cases characters count the no.of uppercases and lower cases without using any methods
print("take a input with both upper and lower cases characters count the no.of uppercases and lower cases without using any methods")
str = input("Enter your string: ")
u_c=0
l_c=0
for i in str:
    if i>='A' and i<='Z':
        u_c+=1
    else:
        l_c+=1
print("Uppercase values:",u_c)
print("Lowercase values:",l_c)

