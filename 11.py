a = int(input())
e = 0
f = 0
g = 0
d = 0
h = 0
for i in range(a):
    b,c = map(int,input().split())
    if b == 0 or c == 0:
        d +=1
    elif b>0 and c>0:
        e += 1 #1
    elif b>0 and c<0:
        f += 1 #4
    elif b<0 and c>0:
        g += 1 #2
    elif b<0 and c<0:
        h += 1 # 3

print("Q1:",e)
print("Q2:",g)
print("Q3:",h)
print("Q4:",f)
print("AXIS:",d)
