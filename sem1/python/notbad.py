s=input("Enter the sentance : ")
a=a.find("not")
b=a.find("bad")
if b>a and a>0 and b>0:
    print(s.lower().replace(s[a:b+4],'good',1))
