# 백준 20055번 컨베이어 벨트 위의 로봇
# GOLD 5
# 알고리즘 분류 : 구현, 시뮬레이션
# 문제 설명이 이상해서 이해하는데 한세월 걸린 문제
# 내 풀이 Python3 시간초과 Pypy3 AC
N,K = map(int,input().split())
A = list(map(int,input().split()))
check = [0]*2*N
ans = 0
while True :
    ans += 1
    A = A[-1:] + A[:2*N-1]
    check = check[-1:] + check[:2*N-1]
    for i in range(2*N-1,-1,-1) :
        if i == 2*N-1 :
            if check[2*N-1] == 1 and check[0] != 1 and A[0] != 0 :
                A[0] -= 1
                check[2*N-1] = 0
                check[0] = 1
        elif check[i] == 1 and check[i+1] != 1 and A[i+1] != 0 :
            A[i+1] -= 1
            check[i] = 0
            check[i+1] = 1
        if check[N-1] == 1 :
            check[N-1] = 0
    if A[0] != 0 and check[0] != 1:
        check[0] = 1
        A[0] -= 1
    if A.count(0) >= K :
        print(ans)
        break

# 다른 풀이
N,K = map(int,input().split())
A = list(map(int,input().split()))
check = [0]*2*N
ans = 0
while True :
    ans += 1
    A = A[-1:] + A[:2*N-1]
    check = check[-1:] + check[:2*N-1]
    for i in range(N-2,-1,-1) :
        check[N-1] = 0
        if check[i] == 1 and check[i+1] != 1 and A[i+1] != 0 :
            A[i+1] -= 1
            check[i] = 0
            check[i+1] = 1
    if A[0] != 0 and check[0] != 1:
        check[0] = 1
        A[0] -= 1

    if A.count(0) >= K :
        print(ans)
        break