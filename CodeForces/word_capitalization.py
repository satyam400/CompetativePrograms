n=input()
if ord(n[0])<91:
    print(chr(ord(n[0]))+n[1:len(n)])
else:
    print(n[0].upper()+n[1:len(n)])