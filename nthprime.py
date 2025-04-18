#Write a program to find user given nth prime with callback function.
def prime_found(prime):
    print(prime)
def n_thprime(n, callback):
    c=0
    m=2
    while True:
        for i in range(2,int(m**0.5)+1):
            if m%i==0:
               break
        else:
            c+=1
            if c==n:
               callback(m)
               return m
        m+=1
n_thprime(5, prime_found)
