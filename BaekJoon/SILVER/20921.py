# 백준 20921번 그렇고 그런 사이
# SILVER 2
# 알고리즘 분류 : 그리디 알고리즘, 구성적
# 이해 못함 조건을 만족하는 것을 먼저 넣고 나머지를 오름차순으로 배열
N,K = map(int,input().split())
li = [0]*N
check = list(range(1,N+1))
idx = 0
for i in range(N-1,0,-1) :
    if K >= i  :
        K -= i
        li[idx] = i+1
        idx += 1
        check[i] = -1
for i in range(N) :
    if check[i] >= 0 :
        li[idx] = check[i]
        idx += 1
print(*li)