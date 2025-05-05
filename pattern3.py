#Print the star in center of square
rows=5
for i in range(rows):
    res=""
    for j in range(rows):
        if i==0 or j==0 or i==rows-1 or j==rows-1 or j==rows//2 and i==j:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
