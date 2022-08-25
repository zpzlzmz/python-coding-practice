a = int(input())
for i in range(a):
    b = int(input())
    e = []
    f = []
    for j in range(b):
        c,d = input().split()
        e.append(int(c))
        f.append(d)       
    print(f[e.index(max(e))])
          
