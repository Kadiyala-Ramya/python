#program to separate odd & even elements from list 
print("program to separate odd & even elements from list ")
list=[1,4,2,7,5,8,9,3]
E_L=[]
O_L=[]
for i in list:
    if i%2==0:
        E_L.append(i)
    else:
        O_L.append(i)
print("Even number list:",E_L)
print("Odd numbers list:",O_L)
print(E_L+O_L)


#program to separate unique elements from list and add "*" at EOL
print("program to separate unique elements from list and add * at duplicate elements ending")
l=[2,3,5,3,6,7,8,4,5]
U_L=[]
D_L=[]
for i in l:
    count=l.count(i)
    if count==1:
        U_L.append(i)
    else:
        D_L.append('*')
print(U_L+D_L)

#program to separate unique elements from list and add "*" at duplicates
l=[2,3,5,3,6,7,8,4,5]
U_L=[]
D_L=[]
for i in l:
    count=l.count(i)
    if count>1:
        U_L.append('*')
    else:
        U_L.append(i)
print(U_L)