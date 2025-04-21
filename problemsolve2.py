#1.find the missing number in the list
l=[2,4,8,12]
m=[]
max_num=max(l)
min_num=min(l)
for i in range(min_num,max_num,2):
    if i not in l:
        m.append(i)
print(m)


#2. Take a dictionary with salaries and Find percentage of the salaries
d={'arjun':30000, 'balaji':35000, 'charan':40000,}
total=0
for v in d.values():
    total+=v
for k,v in d.items():
    a=(v/total)*100
    print(f"{k} has {a:.0f}% of the total")