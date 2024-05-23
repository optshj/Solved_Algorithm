#2775번 부녀회장이 될테야
#BROZNE 1
def fac(a) :
    result = 1
    for i in range(1,a+1):
        result *= i
    return result

a = int(input())
for i in range(a) :
    k = int(input())
    n = int(input())
    print(fac(k+n)//(fac(k+1)*fac(n-1)))
