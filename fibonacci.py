#Write a program to print the count of   number of Fibonacci numbers in between 0 to 500 ?
a=0
b=1
count=0
while a<=500:
    c=a+b
    a=b
    b=c
    count+=1
print(count)