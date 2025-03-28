#1.Write a Python program that takes an integer as input and prints whether it is even or odd.
n=int(input("Enter your number:"))
if n%2==0:
    print("Even number")
else:
    print("Odd number")
#2.Write a program that takes two numbers as input and prints the larger number. If they are equal, print "Both numbers are equal".
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
if a>b:
    print("The largest number is ",a)
elif b>a:
    print("The largest number is ",b)
else:
    print("Both numbers are equal")
#3.Write a Python program that asks the user for a number and prints whether it is positive, negative, or zero.
x=int(input("Enter your number: "))
if x>0:
    print("Positive number")
elif x<0:
    print("Negative number")
else:
    print("zero")
#4.Write a program that asks the user for their age. If the age is 18 or above, print "You are eligible to vote", otherwise print "You are not eligible to vote".
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
"""5.Write a program that takes a student's marks (out of 100) and prints:
"Pass" if marks are 40 or more
"Fail" if marks are less than 40"""
marks=int(input("Enter your marks:"))
if marks<=100:
    if marks>=40:
        print("Pass")
    else:
        print("Fail")
