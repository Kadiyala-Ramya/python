'''Task1: Print the following pattern 
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5 
'''
rows=5
for row in range(1,rows+1):
    s=""
    for col in range(1,rows+1):
        s+=str(row)+" "
    print(s)


'''Task2: Print the following pattern
1 
2 2 
3 3 3
4 4 4 4
5 5 5 5 5
'''
rows=5
for row in range(1,rows+1):
    s=""
    for col in range(row):
        s+=str(row)+" "
    print(s)


'''Print the following pattern
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''
rows=5
for row in range(1,rows+1):
    s=""
    for col in range(1,rows+1):
        s+=str(col)+" "
    print(s)


'''Print the following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
rows=5
for row in range(1,rows+1):
    s=""
    for col in range(1,row+1):
        s+=str(col)+" "
    print(s)