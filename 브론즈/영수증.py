a = int(input())
b = int(input())
add = 0
for i in range(b):
    c,d = map(int,input().split())
    add += c*d
if add == a:
    print("Yes")
else:
    print("No")
