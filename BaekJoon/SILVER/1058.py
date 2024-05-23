# 백준 1058번 친구
# SILVER 3
# 알고리즘 분류 : 그래프, 브루트포스 알고리즘, 플로이드-워셜
N = int(input())
li = [list(input()) for _ in range(N)]
check = [[0]*N for _ in range(N)]
ans = 0
for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if i == j :
                continue
            if li[i][j] == 'Y' :
                check[i][j] = 1
            elif li[i][k] == 'Y' and li[k][j] == 'Y' :
                check[i][j] = 1
for i in check :
    ans = max(ans,sum(i))
print(ans)