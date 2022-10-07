import sys

input = sys.stdin.readline

a = int(input().rstrip())
b = []
c = []
for i in range(a):
    b.append(input().rstrip())
b_list=list(set(b))
for i in b_list:
    c.append(len(i))
d = list(zip(c,b_list))
d.sort()

for i in range(len(d)):
    print(d[i][1])
        
