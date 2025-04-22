#1)Print the multiple of 5 in a list using map and filter 
l=[5,2,10,15,17,19,25]
out=filter(lambda i:i%5==0,l)
out1=map(lambda i:i,out)
print(list(out1))



#2)Print the vowels in the string using map and filter
s="hello world"
v=['a','e','i','o','u']
out=filter(lambda i:i.lower() in v,s)
out1=" ".join(map(str, out))
print(out1)