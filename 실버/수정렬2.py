import sys

a = int(sys.stdin.readline())
b = []
for i in range(a):
    c = int(sys.stdin.readline())
    b.append(c)

b = b.sort()
for i in b:
    print(i)
