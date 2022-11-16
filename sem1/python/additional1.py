a=input("Enter a list of numbers")
a=list(map(int,a.split()))
print("INPUT LIST :",a)
b=[num for num in a if num>100]
print("OUTPUT LIST ",b)
