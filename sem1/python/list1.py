n=input("Enter a list of numbers")
n=list(map(int,n.split()))
positive=[num for num in n if num>0]
print(positive)
n=input("Enter a list of numbers")
n=list(map(int,n.split()))
square=[a**2 for a in n ]
print(square)
n=input("Enter a word")
m=[b for b in n if b.lower() in 'aeiou']
print(m)
x=input("Enter a word")
d=[ord(v) for v in x]
print(d)
n=input("Enter a list of numbers")
n=list(map(int,n.split()))
p=[num for num in n if num%2]
print(p)
n=input("Enter final year :")
p=[year for year in range(2020,int(n)) if(year%400==0) or (year%100 and year%4==0)]
print(p)




