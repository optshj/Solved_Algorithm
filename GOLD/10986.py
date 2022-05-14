# ���� 10986�� ������ ��
# GOLD 3
# �˰����� �з� : ����,���� ��
# �޸� : 185508 KB, �ð� : 1652 ms, ��� Python3, �ڵ���� 340B

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