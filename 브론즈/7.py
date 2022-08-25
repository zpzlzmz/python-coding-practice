a = int(input())
b = input()
b = list(b)
c = 0
d = 0
for i in b:
    if i == "A":
        c+=1
    else:
        d+=1

if c == d:
    print("Tie")
elif c>d:
    print("A")
else:
    print("B")
