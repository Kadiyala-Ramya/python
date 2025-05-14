#task: print the N
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or j==i:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


#Print the letter Z
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


#Print the letter R
rows=5
mid=rows//2
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1:
            res+="* "
        elif j==1:
            res+="* "
        elif j==rows and i<=mid+1:
            res+="* "
        elif i==mid+1:
            res+="* "
        elif i>mid+1 and j==mid+1 and i!=rows:
            res+="* "
        elif i==rows and j==rows:
            res+="* "
        else:
            res+="  "
    print(res)