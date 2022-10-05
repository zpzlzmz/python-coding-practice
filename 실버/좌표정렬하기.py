import sys
input = sys.stdin.readline
a = int(input())
c = []
for i in range(a):
    b = list(map(int,input().split()))
    c.append(b)
c.sort()
for i in range(len(c)):
    print(c[i][0],c[i][1])
