#Print the patterns
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        res+=str(i)+" "
    print(res)

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        res+=str(j)+" "
    print(res)


rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        res+=str(i)+" "
    print(res)

rows=5
for i in range(rows,0,-1):
    res=""
    for j in range(1,i+1):
        res+=str(i)+" "
    print(res)

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        res+=str(j)+" "
    print(res)

rows=5
for i in range(rows,0,-1):
    res=""
    for j in range(1,i+1):
        res+=str(j)+" "
    print(res)

rows=5
for i in range(1,rows+1):
    print(str(i)*i)

rows=5
for i in range(rows,0,-1):
    print(str(i)*i)

n=1
for i in range(1,6):
    res=""
    for j in range(i):
        res+=str(n)+" "
        n+=1
    print(res)