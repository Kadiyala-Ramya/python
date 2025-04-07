#Take a nested list and to find the minimum and maximum values in each sublist
nested=[[1,2,3],[4,5,6],[7,8,9]]
l=[]
s=[]
for i in nested:
    largest=i[0]
    smallest=i[0]
    for j in i:
        if j > largest:
            largest=j
        if j < smallest:
            smallest=j
    l.append(largest)
    s.append(smallest)
print("largest numbers:",l)  
print("smallest numbers:",s)

             