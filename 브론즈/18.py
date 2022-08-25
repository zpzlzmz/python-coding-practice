a1,a2,a3 = map(int,input().split(':'))
b1,b2,b3 = map(int,input().split(':'))
a = (a1*3600) + (a2*60) + a3
b = (b1*3600) + (b2*60) + b3
c = b-a
if c<0:
    c = c+(3600*24)
c1 = c//3600
c2 = (c%3600)//60
c3 = c%60
print("%02d:%02d:%02d" % (c1,c2,c3))
