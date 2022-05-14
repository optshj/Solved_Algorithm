#6588¹ø °ñµå¹ÙÈåÀÇ ÃßÃø
#SILVER 1
import sys
def is_prime(a):
    arr = [True]*(a+1)
    arr[0] - False
    arr[1] = False
    for f in range (2,int(a**0.5)+1):
        if arr[f] == True :
            for j in range(f*2,a+1,f):
                arr[j] = False
    return arr

def check(a,b):
    if prime_list[a] == True and prime_list[b] == True :
        return True
    return False

prime_list = is_prime(1000000)
while True :
    n = int(sys.stdin.readline())
    ans = False 
    if n == 0 :
        break
    for i in range(3,n//2+1,2):
        a = i
        b = n - a
        if check(a,b) :
            print(f'{n} = {a} + {b}')
            ans = True
            break
        else :
            continue
    if ans == False :
        print("Goldbach's conjecture is wrong")