a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#Finding first diagonal elements
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==j:
            print("first diagonal elements:",a[i][j])

#Finding second diagonal elements            
n=3
for i in range(len(a)):
    for j in range(len(a[i])):           
        if i+j==n-1:
            print("second diagonal elements:",a[i][j])

#Maximum length in matrix
b=[
    [1,2,3],
    [4,5,6,7],
    [8,9,10,11,12],
]

n=0
s=[]
for i in range(len(b)):
        if len(b[i])>n:
             n=len(b[i])
             s=b[i]
print("longest sublist: ",s)
print("length of longest sublist: ",n)