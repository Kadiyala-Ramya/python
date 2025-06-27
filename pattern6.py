#print N,Z,H,I patterns
#Print the N pattern
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==j:
            res+="* "
        else:
            res+="  "
    print(res)


#Print the Z pattern
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            res+="* "
        else:
            res+="  "
    print(res)


#Print the H pattern
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==(rows//2)+1:
            res+="* "
        else:
            res+="  "
    print(res)


#Print the I pattern
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==(rows//2)+1:
            res+="* "
        else:
            res+="  "
    print(res)