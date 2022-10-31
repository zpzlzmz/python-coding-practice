import sys
input = sys.stdin.readline

parse = [[0]*101 for i in range(101)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            parse[a+i][b+j] = 1
r = 0
for i in parse:
    r += sum(i)
print(r)

