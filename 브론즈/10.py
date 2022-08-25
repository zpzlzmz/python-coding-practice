
while True:
    a = int(input())
    b = []
    c = "{} =".format(a)
    d = 0 
    for i in range(1,a-1):
        if a%i == 0:
            b.append(i)
            d += i
    for i in range(len(b)):
        c +=" {} +".format(b[i])
    if d ==a:
        c = list(c)
        for i in range(0,2):
            c.pop()
        e = "".join(c)
        print(e)
            
    elif a == -1:
        break
    else:
        print("{} is NOT perfect.".format(a))
