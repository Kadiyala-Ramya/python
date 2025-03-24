#BY Using the While Loop
#Task 1 : Find the second prime of the given number ?
print("Find the second prime of the given number")
n=int(input("Enter your number:"))
while True:
    n+=1
    for i in range(2,n,1):
        if n%i==0:
            break
    else:
        print("Next prime number:",n)
        break
#By using break control statement
#Task 2 : Break the loop if  Condition matches with the given number?
print("Break the loop if  Condition matches with the given number")
i=1
while i<10:
    print(i)
    if i==5:
        break
    i+=1
#By using the continue control statement
#Task 3 : Print the numbers from 1 to 100, but it should not print multiples of 3?
print("Print the numbers from 1 to 100, but it should not print multiples of 3")
i=0
while i<100:
    i+=1
    if i%3==0:
        continue
    print(i)
        