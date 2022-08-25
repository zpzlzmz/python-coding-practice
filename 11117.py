a1=[]
b1=[]
c=[]
for i in range(10):
    a,b = map(int,input().split())
    a1.append(a)
    b1.append(b)
    c.append(sum(b1)-sum(a1))
print(max(c))
