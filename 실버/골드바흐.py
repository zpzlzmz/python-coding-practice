b = []
for i in range(1, 10000):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        b.append(i)
a = int(input())

for i in range(a):
    c = int(input())
    A = int(c/2)
    B = c-A
    for i in range(c):
        if A in b and B in b:
            print(A,B)
            break
        else:
            A -= 1
            B += 1
    
