import sys
a = int(sys.stdin.readline())
sum1 = 0
for i in range(a):
    b = int(sys.stdin.readline())
    if i == (a-1):
        sum1 += b
    else:
        sum1 += (b-1)
print(sum1)
