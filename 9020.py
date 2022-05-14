#9020¹ø °ñµå¹ÙÈåÀÇ ÃßÃø
#SILVER 1
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

li = []    
for f in range(2,5001) :
    if verf(f) :
        li.append(f)
a = int(sys.stdin.readline())
for i in range(a) :
    b = int(sys.stdin.readline())
    gap = b - 4
    m = 2
    n = b - 2
    for k in li :
        if k > b//2 :
            break

        if verf(b-k) and gap > b-2*k :
            gap = b-2*k
            m = k
            n = b - k
    print(f'{m} {n}')