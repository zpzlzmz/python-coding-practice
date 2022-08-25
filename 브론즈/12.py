a = int(input())
f = 0
o = 0
t = 0

if a%10 != 0:
    print(-1)
    exit()
else:
    o = a//60
    t = (a%60)//10
    f = o//5
    o = o-f*5
    
print(f,o,t)
