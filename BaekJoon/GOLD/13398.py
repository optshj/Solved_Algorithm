# 백준 13398번 연속합 2
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
# 0은 제거된게 없는경우 1은 제거된게 있는 경우
# 1에서 제거한게 제거안한거 보다 크면 제거한걸 선택
N = int(input())
li = list(map(int,input().split()))
dp = [[0]*N for _ in range(2)]
dp[0][0] = li[0]
dp[1][0] = li[0]
for i in range(1,N) :
    dp[0][i] = max(dp[0][i-1]+li[i],li[i])
    dp[1][i] = max(dp[1][i-1] + li[i],dp[0][i-1])
print(max(max(dp[0]),max(dp[1])))