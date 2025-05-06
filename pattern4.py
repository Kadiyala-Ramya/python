#task1: Print the pattern
# 55555
4444
333
22
1

rows=5
for i in range(rows,0,-1):
    res=""
    for j in range(i,0,-1):
        res+=str(i)+" "
    print(res)


#task2: Print the pattern
#* * * * *
# * * * *
#  * * *
#   * *
#    *

rows=5
for i in range(1,rows+1):
    res=""
    for sp in range(i-1):
        res+=" "
    for j in range(rows-i+1):
        res+="*"+" "
    print(res)



#task3: Print the pattern
# *       *
# *       *
# * * * * *
# *       *
# *       *
rows=5
mid=rows//2
for i in range(rows):
    res=""
    for j in range(rows):
        if i==mid or j==0 or j==rows-1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)