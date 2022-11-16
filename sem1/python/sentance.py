str1=input("Enter the string")
n= " "
for x in str1:
    if(x.isalpha() or x==' '):
        n+=x
print(len(n.split()))
