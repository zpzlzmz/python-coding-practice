a = int(input())
b = int(input())
c = 0
d=[]
for i in range(a,b+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        if i == 1:
            continue
        else:
            c += i
            d.append(i)

if c == 0 or c == 1:
    print(-1)
else:
    print(c)
    print(d[0])
