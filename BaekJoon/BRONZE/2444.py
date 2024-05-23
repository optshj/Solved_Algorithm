#2444¹ø º° Âï±â - 7
#BRONZE 3
import sys
a = int(sys.stdin.readline())
for i in range(1,a) :
    print(" "*(a-i)+"*"*(2*i-1))
for i in range(a,0,-1) :
    print(" "*(a-i)+"*"*(2*i-1))