#1934�� �ּҰ����
#SILVER 5
T = int(input())
for i in range(T):
    a , b = map(int,input().split())
    A = a
    B = b
    if a > b :
        a , b = b , a
    gcd = a
    while b%gcd :
        r = b%gcd
        b , gcd = gcd , r
    print(A*B//gcd)