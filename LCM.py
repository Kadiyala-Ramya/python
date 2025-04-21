#Write a program to find LCM for 3 numbers.
#LCM of 3 numbers
a=2
b=3
c=4
max_num=max(a,b,c)
while True:
    if max_num%a==0 and max_num%b==0 and max_num%c==0:
        print("LCM:",max_num)
        break
    max_num+=1