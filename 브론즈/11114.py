a = 0
b = 1
c = int(input())
d = 0
for i in range(1,c):
    d = a+b
    a = b
    b = d
if c == 1:
    print(1)
else:
    print(d)
