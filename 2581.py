#2581¹ø ¼Ò¼ö
#SILVER 5
import sys
def verf(i) :
    v = 2
    if i == 1 :
        return False
    while i >= v*v :
        if i%v == 0 :
            return False
        v += 1
    return True

m = int(input())
n = int(input())
result = 0
min = 0
for i in range(m,n+1)  :
    if min == 0 :
        if verf(i):
            result += i
            min = i
    else :
        if verf(i):
            result += i
if result >= 1 :
    print(result)
    print(min)
else :
    print(-1)
