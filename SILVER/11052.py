# 백준 11052번 카드 구매하기
# SILVER 1
# 알고리즘 분류 : 다이나믹 프로그래밍
N = int(input())
P = [0] + list(map(int,input().split()))
for i in range(1,N+1) :
    res = []
    for j in range(i//2+1) :
        res.append(P[j] + P[i-j])
    P[i] = max(res)
print(P[-1])