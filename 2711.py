#2711번 오타맨 고창영
#BRONZE 2
a = int(input())
for i in range(a) :
    m , n = map(str,input().split())
    m = int(m) - 1
    n = list(n)
    del n[m]
    print(''.join(n))