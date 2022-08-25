a=int(input())
b=int(input())
c=int(input())

d = str(a*b*c)

d = list(map(int,str(d)))

for i in range(10):
    e = 0
    for j in range(len(d)):
        if i == d[j]:
            e += 1
    print(e)
