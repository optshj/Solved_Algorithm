# 백준 2565번 전깃줄
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
# 증가하는 최장부분수열을 구하면 되는 문제 -> 교차하지 않는 젓깃줄의 개수

N = int(input())
li = sorted([list(map(int,input().split())) for _ in range(N)])
dp = [0]*(N+1)
for i in range(N) :
    max_val = 0
    for j in range(i) :
        if li[i][1] > li[j][1] :
            if dp[j+1] > max_val :
                max_val = dp[j+1]
    dp[i+1] = max_val + 1
print(N - max(dp))