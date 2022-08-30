### 걍 무지성으로 해봄
## 실패
##a,b = map(int,input().split())
##count = 0
##for i in range(a,b+1):
##    c = []
##    if i == 1:
##        continue
##    for j in range(2,i):
##        if i%j == 0:
##            break
##    else:
##        print(i)

#구글링 - 에라토스테네스의 체 - 소수 구하기
a,b = map(int,input().split())

for i in range(a,b+1):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        print(i)
