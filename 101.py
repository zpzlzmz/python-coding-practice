a,b = map(int,input().split())
c =[]
d = 0
e = 0
for i in range(1,min(a,b)+1):
    if a%i ==0 and b%i == 0:
        c.append(i)
for i in range(1,a*b+1):
    if a==1 and b == 1:
        d = 1
        break
    else:
        d = max(a,b)*i
        if d%(min(a,b)) == 0:
            break

print(max(c))
print(d)
