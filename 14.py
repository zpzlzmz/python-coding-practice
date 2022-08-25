a = int(input())
for j in range(a):
    d = 0
    e = 0
    for i in range(0,9):
        b,c = map(int,input().split())
        d += b
        e += c

    if d>e:
        print("Yonsei")
    elif d<e:
        print("Korea")
    else:
        print("Draw")
