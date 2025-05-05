'''task:Print the following pattern
a
b c 
d   f
g     j
k l m n o'''

rows=5
code=97
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        if j==1 or j==i or i==rows:
            res+=chr(code)+" "
        else:
            res+="  "
        code+=1
    print(res)





