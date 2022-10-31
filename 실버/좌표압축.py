import sys
input = sys.stdin.readline
##a = int(input())
## 처음에 한 뻘짓 
##b = list(map(int,input().split()))
##c=[]
##d = []
##for i in range(len(b)):
##    c.append(i)
##
##all_c = list(zip(b,c))
##
##for i in range(len(all_c)):
##    all_c[i] = list(all_c[i])
##
##all_c.sort(key=lambda x:x[0])
##
##for i in range(len(all_c)):
##    ###### 비교한 후 같으면 번호도 같게 설정해야함 .
##    d.append(i)
##
##all_d = list(zip(all_c,d))
##
##for i in range(len(all_d)):
##    all_d[i] = list(all_d[i])

a = int(input()) # 공략좀 찾아봄 

b = list(map(int,input().split()))

b1 = set(b)
a = list(b1)
a.sort()

numa = {}
for i in range(len(a)):
    numa[a[i]] = i
for i in b:
    print(numa[i],end = ' ')
