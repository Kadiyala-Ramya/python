#1.implement the count method on a list by taking input from user without using actual method.
l = input("Enter elements separated by space: ").split()
count=0
for i in l:
    count=count+1
print("No.of elements in the list are:", count)
#2.implement the copy method on a list just as the above condition.
m = input("Enter elements separated by space:").split()
n=m.copy()
print("New list:", n)
#3.Implement the program to print true when the first and last element in the list was even, else print false.
l=[2,3,4,5,6,7]
f_l=l[0]%2
l_l=l[-1]%2
if f_l==0 and l_l==0:
    print("True")
else:
    print("False")
#4. write a program to print the prime numbers in the new list from the existing list.
E_L=[9,8,5,7,2,12,15]
N_L=[]
for i in E_L:
    if i>1:
        is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        N_L.append(i)
print("Prime numbers in the new list:",N_L)
