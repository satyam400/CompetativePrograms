a=[]
for i in range(0,5):
    a.append([int(j) for j in input().split()])

for i in range(0,5):
    for j in range(0,5):
        if a[i][j]!=0:
            b=i
            c=j

print(max(b,2)-min(b,2)+max(c,2)-min(c,2))