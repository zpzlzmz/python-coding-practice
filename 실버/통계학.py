import math
from collections import Counter
import sys

a = int(sys.stdin.readline())
b = []

for i in range(a):
    c =int(sys.stdin.readline())
    b.append(c)
b.sort()
print(round(sum(b)/a))
if int(len(b))%2 == 0:
    print(b[a/2-1])
else:
    print(b[int(a/2)])
c = Counter(b).most_common()
if len(c) == 1:
    print(c[0][0])
else:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])

print(max(b)-min(b))

