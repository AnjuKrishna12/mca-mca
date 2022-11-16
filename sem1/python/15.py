s=input("Enter the sentance ")
w={}
for word in s.upper().split():
    w[word]=w.get(word,0)+1
print(w)
    
