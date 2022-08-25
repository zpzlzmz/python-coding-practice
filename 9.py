##a = input()
##
##if a == a[::-1]:
##    print(1)
##else:
##    print(0)
##c = 0
##while True:
##    a,b = map(int,input().split())
##    if a<=b:
##        for i in range(5):
##            if b%a == 0:
##                print("factor")
##                break
##            c = b%a
##            b = a
##            a = c
##            if a<=1:
##                print("neither")
##    elif a>b:
##        if a%b == 0:
##            print("multiple")
##            break
##        elif a%b != 0:
##            print("neither")
##            break
##    elif a == 0 and b == 0:
##        break

while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    if b%a == 0:
        print('factor')
    elif a%b == 0:
        print("multiple")
    else:
        print('neither')
            
