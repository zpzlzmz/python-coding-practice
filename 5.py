a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())
g = []
if a == c:
    g.append(e)
elif c == e:
    g.append(a)
elif a == e:
    g.append(c)
if b == d:
    g.append(f)
elif b==f:
    g.append(d)
elif d == f:
    g.append(b)
    
print(int(g[0]),int(g[1]))
