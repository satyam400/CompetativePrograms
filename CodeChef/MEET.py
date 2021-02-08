t = int(input())
for i in range(0, t):
    p = input().split()
    x = ""
    q = p[0].split(":")
    n = int(input())
    if p[1] == "AM" and int(q[0]) == 12:
        a = (12 - int(q[0])) * 60 + int(q[1])
    elif p[1] == "AM" and int(q[0]) != 12:
        a = (int(q[0])) * 60 + int(q[1])
    elif p[1] == "PM" and int(q[0]) == 12:
        a = (12 - int(q[0])) * 60 + int(q[1]) + 720
    elif p[1] == "PM" and int(q[0]) != 12:
        a = (int(q[0])) * 60 + int(q[1]) + 720

    for j in range(0, n):
        r = [x for x in input().split()]
        s = r[0].split(":")
        t = r[2].split(":")

        b = 0
        c = 0
        if r[1] == "PM" and int(s[0]) != 12:
            b = int(s[0]) * 60 + int(s[1]) + 720

        elif r[1] == "PM" and int(s[0]) == 12:
            b = (12 - int(s[0])) * 60 + int(s[1]) + 720

        elif r[1] == "AM" and int(s[0]) != 12:
            b = int(s[0]) * 60 + int(s[1])

        elif r[1] == "AM" and int(s[0]) == 12:
            b = (12 - int(s[0])) * 60 + int(s[1])

        if r[3] == "PM" and int(t[0]) != 12:
            c = int(t[0]) * 60 + int(t[1]) + 720

        elif r[3] == "PM" and int(t[0]) == 12:
            c = (12 - int(t[0])) * 60 + int(t[1]) + 720

        elif r[3] == "AM" and int(t[0]) != 12:
            c = (int(t[0])) * 60 + int(t[1])

        elif r[3] == "AM" and int(t[0]) == 12:
            c = (12 - int(t[0])) * 60 + int(t[1])

        if b <= a <= c:
            x = x + "1"
        else:
            x = x + "0"

    print(x)
