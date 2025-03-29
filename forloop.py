#1.take input number from user and print the factors of that number
a=int(input("Enter your number:"))
print("Factors of the number")
for i in range(1,a+1,1):
    if a%i==0:
        print(i)
#2.print the tables from 1-5 with multiplying of even numbers
for i in range(1,6,1):
    for j in range(2,11,2):
        print(i,"x",j,"=",i*j)