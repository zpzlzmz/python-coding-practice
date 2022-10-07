import sys
a = int(sys.stdin.readline())
c=[]
d=[]
e=[]
f=[]
for i in range(a):
    b = list(map(int,sys.stdin.readline().split()))
    c.append(b)
for i in range(len(c)):
    d.append(c[i][0])
    e.append(c[i][1])
f = list(zip(e,d))
f.sort()
d=[]
e=[]
for i in range(len(f)):
    d.append(f[i][0])
    e.append(f[i][1])
c = list(zip(e,d))
for i in range(len(c)):
    print(c[i][0],c[i][1])
