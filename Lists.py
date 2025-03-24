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