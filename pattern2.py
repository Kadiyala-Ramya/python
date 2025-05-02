'''task:Print the following pattern
a
b c 
d   f
g     j
k l m n o'''

rows=5
code=97
for i in range(rows):
    res=""
    for j in range(rows):
        if i==rows-1 or j==0 or j==i:
            res+=chr(code)+" "
            code+=1
        else:
            res+=" "+" "
    print(res)

