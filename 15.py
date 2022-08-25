a = int(input())
d = []
e = []
g = []
h = 0
for i in range(a):
    f = int(input())
    for j in range(f):
        b,c = input().split()
        d.append(b)
        e.append(c)
    for j in range(len(e)):
        g.append(int(e[j]))
    h=g.index(max(g))
    print(d[h])
