import sys

input = sys.stdin.readline
a = int(input())
b = []
c = []
for i in range(a):
    b.append(list(input().split()))
for i in range(len(b)):
    b[i][0] = int(b[i][0])   
b.sort(key=lambda x:x[0])
for i in range(len(b)):
    print(b[i][0],b[i][1])
