a = input()
a = list(a)
c = 10
for i in range(0,len(a)-1):
    if a[i] == a[1+i]:
        c +=5
    else:
        c+=10
print(c)
