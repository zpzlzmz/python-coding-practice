a = []

for _ in range(int(input())):
    n,d,m,y = input().split()

    a.append([n,int(d),int(m),int(y)])
a.sort(key = lambda x:(x[3],x[2],x[1]))
print(a[4][0])
print(a[0][0])
