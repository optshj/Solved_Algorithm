# 백준 17626번 Four Squares
# SILVER 4
# 알고리즘 분류 : 다이나믹 프로그래밍,브루트포스 알고리즘
# 메모리 : 114880KB, 시간 : 148ms, 언어 : PyPy3, 코드 길이 : 249B
N = int(input())
dp = [0]*(N+1)
for i in range(1,N+1) :
    if i**0.5 == int(i**0.5) :
        dp[i] = 1
    else :
        mv = 50000
        for j in range(1,int(i**0.5)+1) :
            mv = min(mv,dp[i-j**2])
        dp[i] = mv + 1
print(dp[-1])