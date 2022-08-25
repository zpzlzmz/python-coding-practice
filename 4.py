a = int(input())
e = []
for i in range(a):
    b,c,d = map(int,input().split())
    if b == c and b == d:
        e.append(10000+b*1000)
    elif b == c or b == d:
        e.append(1000+b*100)
    elif c == d:
        e.append(1000+c*100)
    elif b != c and b != d and c != d:
        e.append(max(b,c,d)*100)

print(max(e))
