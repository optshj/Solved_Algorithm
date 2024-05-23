#2445¹ø º° Âï±â - 8
#BRONZE 3
import sys
a = int(sys.stdin.readline())
for i in range(1,a) :
    print('*'*i+' '*(2*a-2*i)+'*'*i)
for i in range(a,0,-1) :
    print('*'*i+' '*(2*a-2*i)+'*'*i)