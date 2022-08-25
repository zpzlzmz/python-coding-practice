a = int(input())

for i in range(a):
    b = int(input())
    c1 = []
    d1 = []
    e = 0
    for j in range(0,b):
        c,d = input().split()
        c1.append(int(c))
        d1.append(float(d))
        e+= c1[j]*d1[j]
    print(sum(c1),"{:.1f}".format(e/sum(c1)))   
        
        
