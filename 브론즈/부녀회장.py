a = int(input())

for _ in range(a):
    b = int(input())
    c = int(input())
    d = [x for x in range(1,c+1)]

    for j in range(b):
        for i in range(1,c):
            d[i] += d[i-1]
    print(d[-1])
    
    ## d = [[],[]]이런식으로 구분해서 하려고 했는데, 이런 방법이 있었네
