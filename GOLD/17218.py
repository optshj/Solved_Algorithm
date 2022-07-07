# 백준 17218번 비밀번호 만들기
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
a = input()
b = input()
dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]
for i in range(len(b)) :
    for j in range(len(a)) :
        if a[j] == b[i] :
            dp[i+1][j+1] = dp[i][j] + 1
        else :
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
ans = ''
a_len = len(a)
b_len = len(b)
while dp[b_len][a_len] != 0 :
    if dp[b_len-1][a_len] == dp[b_len][a_len] :
        b_len -= 1
    elif dp[b_len][a_len] == dp[b_len][a_len-1] :
        a_len -= 1
    else :
        ans += a[a_len-1]
        a_len -= 1
        b_len -= 1
print(ans[::-1])