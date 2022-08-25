a = int(input())
d = 100 # b
e = 100 # c
for i in range(a):
    b,c = map(int,input().split())
    if b == c:
        pass
    elif b>c:
        e = e-b
    elif b<c:
        d = d-c
    else:
        pass
print(d)
print(e)
