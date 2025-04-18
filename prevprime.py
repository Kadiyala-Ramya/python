#To print the previous prime number to that number
n=int(input("Enter your number:"))
if n>0:
    while True:
        n-=1
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            print("Previous prime number",n)
            break
