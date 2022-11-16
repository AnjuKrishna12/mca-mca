s=input("Enter the String")
if s.lower().endswith("ing"):
    s+="ly"
else:
    s+="ing"
print(s)

