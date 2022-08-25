##b = []
##for i in range(10):
##    a = int(input())
##    b.append(a)
##print(int(sum(b)/10))
##f = 0
##f = max(set(b),key=b.count)
##print(f)

##a = int(input())
##
##for i in range(a):
##    b,c = input().split()
##    b = int(b)
##    c = list(c)
##    del c[b-1]
##    print(''.join(c).upper())

##b=[]
##for i in range(5):
##    for j in range(4):
##        a = list(map(int,input().split()))
##        b.append(sum(a))  
##        break 
##
##print(b.index(max(b))+1)
##print(max(b))

##a,b = map(int,input().split())
##c=[]
##d = 0
##for i in range(46):
##    for j in range(i):
##        c.append(i)
##for i in range(a,b+1):
##    d += c[i-1]
##print(d)

##a = int(input())
##c = []
##for i in range(a):
##    b = int(input())
##    b = format(b,'b')
##    b = list(b)
##    b.reverse()
##    for i in range(len(b)):
##        if b[i] == '1':
##            c.append(i)
##for i in range(len(c)):
##    print(c[i],end = " ")

##a = int(input())
##b = list(map(int,input().split()))
##c = int(input())
##d = []
##for i in b:
##    if i == c:
##        d.append(i)
##print(len(d))



##scoreSort = []
##score = []
##for i in range(8):
##    data = int(input())
##    score.append(data)
##    scoreSort = sorted(score,reverse=True)
##scoresum = 0
##d = []
##for i in range(5):
##    scoresum += scoreSort[i]
##    for j in range(8):
##        if scoreSort[i] == score[j]:
##            d.append(score.index(score[j])+1)
##print(scoresum)
##d.sort()
##for i in range(5):
##    if i == 4:
##        print(d[i])
##    else:
##        print(d[i],end=" ")

##a = int(input())
##b1 = []
##for i in range(a):
##    b = int(input())
##    b1.append(b)
##    b1.sort()
##for i in b1:
##    print(i)

##d=[]
##a,b,c = map(int,input().split())
##d.append(a)
##d.append(b)
##d.append(c)
##d.sort()
##for i in range(3):
##    if i == 2:
##        print(d[i])
##    else:
##        print(d[i],end=" ")


##a = int(input())
##b = list(map(int,input().split()))
##print(min(b)*max(b))

##b = []
##c = []
##d = []
##for i in range(5):
##    a = int(input())
##    b.append(a)
##c = b[:3]
##d = b[3:]
##print(min(c)+min(d)-50)

##b=[]
##for i in range(5):
##    a = int(input())
##    b.append(a)
##    b.sort()
##print(int(sum(b)/5))
##print(b[2])


##a = input()
##a = list(a)
##a.sort(reverse=True)
##for i in a:
##    print(int(i),end="")

##b = []
##for i in range(9):
##    a = int(input())
##    b.append(a)
##b.sort()
##for i in range(8):
##    if len(b)<8:
##        break
##    for j in range(i+1,9):
##        q = b[i] + b[j]
##        if sum(b)-q == 100:
##            b.remove(b[i])
##            b.remove(b[j-1])
##            break
##for i in b:
##    print(int(i))

##a = int(input())
##for i in range(a):
##    c = []
##    b = list(map(int,input().split()))
##    for j in b:
##        if j % 2 == 0:
##            c.append(j)
##    print(sum(c), min(c))

##a = int(input())
##
##for i in range(a):
##    b = list(map(int,input().split()))
##    c1 = []
##    print("Class {}".format(i+1))
##    del b[0]
##    b.sort()
##    for j in range(len(b)-1):
##        c = b[j+1]-b[j]
##        c1.append(c)
##    print("Max {}, Min {}, Largest gap {}".format(max(b),min(b),max(c1)))

##b = []
##c = []
##for i in range(10):
##    a = int(input())
##    b.append(a)
##for i in range(10):
##    a = int(input())
##    c.append(a)
##b.sort(reverse=True)
##c.sort(reverse=True)
##print(sum(b[:3]),sum(c[:3]))

##d = []
##e1 = []
##count,money = map(int,input().split())
##
##for i in range(count):
##    coin = int(input())
##    d.append(coin)
##    
##d.sort(reverse=True)
##
##for i in range(count):
##    if money == 0:
##        break
##    e = money//d[i]
##    e1.append(e)
##    money = money%d[i]
##print(sum(e1))

##a = list(input())
##print(len(a))

##a = list(input())
##b = []
##for i in a:
##    if i == i.upper():
##        b.append(i.lower())
##    elif i == i.lower():
##        b.append(i.upper())
##for i in range(len(b)):
##    print(b[i],end="")

##a = int(input())
##
##for i in range(a):
##    b,c = map(int,input().split(","))
##    print(b+c)


##a = input()
##a1 = list(a)
##b=[]
##b.append(a1[0])
##for i in range(len(a1)):
##    if a1[i] == '-':
##        b.append(a1[i+1])
##for i in range(len(b)):
##    print(b[i],end="")

##a,b = input().split()
##a1 = list(a)
##b1 = list(b)
##a1.reverse()
##b1.reverse()
##a = "".join(a1)
##b = "".join(b1)
##c = int(a)+int(b)
##c1 = list(str(c))
##c1.reverse()
##for i in range(len(c1)):
##    if c1[0] == "0":
##        del c1[0]
##    else:
##        break
##print("".join(c1))

##a = input()
##count = 0
##b = ['a','e','i','o','u']
##for i in range(len(a)):
##    for j in range(len(b)):
##        if a[i] == b[j]:
##            count += 1
##print(count)

##a = int(input())
##
##for i in range(a):
##    b = input()
##    b = list(b)
##    b[0] = b[0].upper()
##    print("".join(b))

##a = input()
##a = list(a)
##b = 0
##c = 10
##for i in range(10):
##    print("".join(a[b:c]))
##    if c == 100:
##        break
##    elif len(a[b:c])<10:
##        break
##    b = c
##    c += 10
    
##a = list(map(int,input().split(",")))
##print(len(a))


##a = input()
##a = list(a)
##b = []
##for i in range(97,123):
##    count = 0
##    for j in a:
##        if j == chr(i):
##            count += 1
##    b.append(count)
##for i in range(len(b)):
##    print(int(b[i]),end=" ")


##a = int(input())
##for i in range(a):
##    c = []
##    a,b = input().split()
##    a = list(a)
##    b = list(b)
##    for i in range(len(a)):
##        if ord(b[i])-ord(a[i]) >= 0:
##            c.append(ord(b[i]) - ord(a[i]))
##        elif ord(b[i])-ord(a[i]) < 0:
##            c.append(ord(b[i])-ord(a[i]) + 26)
##    print("Distances: ",end= "")
##    for i in range(len(c)):
##        if i == (len(c)-1):
##            print(c[i],end="")
##        else:
##            print(c[i],end=" ")
##    print()

##a = int(input())
##
##for i in range(a):
##    b = input()
##    if len(b)<=1:
##        print(b[0])*2,sep=""))
##    else:
##        print(b[0],b[-1],sep="")

##a = 30
##for i in range(a):
##    b = input()
##    if b == "END":
##        break
##    b = list(b)
##    b.reverse()
##    for j in range(len(b)):
##        print(b[j],end="")
##    print()

##a = int(input())
##
##for i in range(a):
##    b,c = map(int,input().split())
##    count = 0
##    for j in range(b,c+1):
##        d = list(str(j))
##        for k in d:
##            if k == "0":
##                count += 1
##    print(count)

##for _ in range(int(input())):
##    b,e = map(int,input().split())
##    s = 0
##    for i in range(b,e+1):
##        s += str(i).count("0")
##    print(s)

##sentence = input()
##LS = list(sentence)
##for i in range(len(LS)):
##    if 65 <= ord(LS[i]) <= 90:
##        LS[i] = ord(LS[i]) + 13
##        if LS[i] > 90:
##            LS[i] = LS[i] - 26
##    elif 96 < ord(LS[i]) <= 122:
##        LS[i] = ord(LS[i]) + 13
##        if LS[i] > 122:
##            LS[i] = LS[i] - 26
##    elif 48 <= ord(LS[i]) <= 57:
##        LS[i] = ord(LS[i])
##        pass
##    else:
##        pass
## 
##for i in range(len(LS)):
##    if LS[i] == " ":
##        print(" ",end="")
##    else:
##        print(chr(LS[i]),end="")

##a = int(input())
##b = 1
##
##d = 0
##for i in range(1,a+1):
##    b *= i
##c = list(str(b))
##c.reverse()
##for i in range(len(c)):
##    if c[i] == "0":
##        d +=1
##    else:
##        break
##print(d)
##
