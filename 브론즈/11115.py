b = []
c = []
for i in range(7):
    a = int(input())
    b.append(a)
for i in b:
    if i % 2 != 0:
        c.append(i)
if len(c) == 0:
    print(-1)
else:
    print(sum(c))
    print(min(c))
