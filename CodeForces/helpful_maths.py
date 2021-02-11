n=input()
l=[]
for i in range(0,len(n)):
    if i%2==0:
        l.append(int(n[i]))
l.sort()
s=""
for j in range(0,len(l)):
    s+=str(l[j])+"+"
print(s[0:len(s)-1])