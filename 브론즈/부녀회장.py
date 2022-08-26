a = int(input())

for _ in range(a):
    b = int(input())
    c = int(input())
    d = [x for x in range(1,c+1)]

    for j in range(b):
        for i in range(1,c):
            d[i] += d[i-1]
    print(d[-1])
