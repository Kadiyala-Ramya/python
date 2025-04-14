#Task:- Task1 Take 9 digit number,take one digit check whether that digit is present or not , print the count of that digit and positions
a=243544536
b=str(a)
pos=[]
d='4'
for i in range(len(b)):
    if b[i]==d:
        pos.append(i)
print("Count of digit:",len(pos))
print("Positions of digit:",pos)


#Task2: Take a number check whether that no is in descending order or not
a = '123'
desc = True
for i in range(len(a)):
    if a[i] < a[i-1]:
        desc = False
        break
if desc:
    print("the number is  in descending order")
else:
    print("the number is not in descending order")
