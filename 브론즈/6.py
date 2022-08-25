a = int(input())

for i in range(a):
    b,c,d = map(int,input().split())
    if (b+d)>c:
        print("do not advertise")
    elif (b+d) == c:
        print("does not matter")
    else:
        print("advertise")
