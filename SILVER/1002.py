#1002¹ø ÅÍ·¿
#SILVER 4
import sys
a = int(input())
for i in range(a) :
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    ran = ((x1-x2)**2+(y1-y2)**2)**0.5
    if x1 == x2 and y1 == y2 and r1 == r2 :
        print(-1)
    elif ran + r1 == r2 :
        print(1)
    elif ran + r1 < r2 :
        print(0)
    elif ran + r2 == r1 :
        print(1)
    elif ran + r2 < r1 :
        print(0)        
    elif ran == r1+r2 :
        print(1)
    elif ran < r1+r2 :
        print(2)
    elif ran > r1+r2 :
        print(0)