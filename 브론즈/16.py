import math
a = int(input())
b = int(input())
d = []
e = 0
for i in range(a,b+1):
    c = math.sqrt(i)
    if c%int(c) == 0:
        d.append(i)

if len(d) == 0:
    print(-1)
else:
    for i in d:
        e += i
    print(e)
    print(min(d))
