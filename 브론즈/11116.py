a = int(input())
b = list(map(int,input().split()))
sum1 = 0
count = 0
for i in b:
    if i == 1:
        count +=1
        sum1 += count
    elif i == 0:
        count = 0
print(sum1)
