a = int(input()) #12

b = a//5 # 2
c = a%5 # 2

for i in range(b+1):
    if c == 0:
        print(b)
        break
    elif c%3 != 0:
        b -= 1
        c += 5
        if b == -1:
            print(-1)
    elif c%3 == 0:
        print(b+(c//3))
        break
