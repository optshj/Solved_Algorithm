# 백준 9471번 피사노 주기
# SILVER 4
# 알고리즘 분류 : 수학, 정수론
# 2749번에서 나온 피사노 주기를 활용한 문제
P = int(input())
for _ in range(P) :
    N,M = map(int,input().split())
    a,b = 0,1
    cnt = 0
    while True :
        if a%M == 1 and b%M == 0 :
            break
        cnt += 1
        a,b = b , (a+b)%M
    print(f"{N} {cnt+1}")