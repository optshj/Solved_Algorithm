#2522¹ø º° Âï±â - 12
#BRONZE 3
import sys
a = int(sys.stdin.readline())
for i in range(1,a+1) :
    print(' '*(a-i)+'*'*(i))
for i in range(1,a) :
    print(' '*(i)+'*'*(a-i))