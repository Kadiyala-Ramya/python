#1. Print the list of prime numbers and non prime numbers separately in given list.
E_L=[9,8,5,7,2,12,15]
P_L=[]
N_L=[]
for i in E_L:
    if i>1:
        is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        P_L.append(i)
    else:
        N_L.append(i)
print("Prime numbers in the new list:",P_L)
print("Non prime numbers in the new list:",N_L)


#2. Count the skills through the dictionary.
S_L = ['Python', 'Java', 'Python', 'C++', 'Java', 'Python', 'JavaScript', 'C++', 'Python']

skills_count = {}

for skill in S_L:
    if skill in skills_count:
        skills_count[skill] += 1
    else:
        skills_count[skill] = 1

print("Skill count:", skills_count)
