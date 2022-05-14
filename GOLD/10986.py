# 백준 10986번 나머지 합
# GOLD 3
# 알고리즘 분류 : 수학,누적 합
# 메모리 : 185508 KB, 시간 : 1652 ms, 언어 Python3, 코드길이 340B

N,M = map(int,input().split())
li = list(map(int,input().split()))
cnt = 0
dp = [0]*N
num = [-1]*M

num[0] = 0
li[0] = li[0]%M
num[li[0]] += 1
dp[0] = [li[0],num[li[0]%M]]

for i in range(1,N) :
    li[i] = (li[i-1] + li[i])%M
    num[li[i]] += 1
    dp[i] = [li[i],num[li[i]]]
    
for i in range(0,N) :
    cnt += dp[i][1]

print(cnt)