#2446¹ø º° Âï±â - 9
#BRONZE 3
import sys
a = int(sys.stdin.readline())
for i in range(0,a) :
    print(' '*i+'*'*(2*a-2*i-1))
for i in range(a-2,-1,-1) :
    print(' '*i+'*'*(2*a-2*i-1))