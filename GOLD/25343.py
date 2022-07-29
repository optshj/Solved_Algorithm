# 백준 25343번 최장 최장 증가 부분 수열
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
ans = 0
for i in range(N) :
    for j in range(N) :
        max_val = 0
        for m in range(i+1) :
            for n in range(j+1) :
                if li[m][n] < li[i][j] :
                    max_val = max(max_val,dp[m][n])
        dp[i][j] = max_val + 1
        ans = max(ans,dp[i][j])
print(ans)