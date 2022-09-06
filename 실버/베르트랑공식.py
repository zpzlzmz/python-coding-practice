b = []
for i in range(1,246913):
        if i == 1:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            b.append(i)
while True:
    n = int(input())
    count = 0
    if n ==0:
        break
    for i in range(len(b)):
            if int(b[i])>n and int(b[i])<=(n*2):
                count += 1
    print(count)
