#Task1:Print the prime digits in the given number
a=135679
b=str(a)
P_L=[]
for i in b:
    if i in ('2','3','5','7'):
        P_L+=i
print("Prime digits in the number are","".join(P_L))
#Task2:Practice Armstrong number program
n=int(input("Enter your number:"))
s=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10
if s==sum:
    print("Armstrong number")
else:
    print("Not a armstrong number")

