# 백준 11444번 피보나치 수 6
# GOLD 2
# 알고리즘 분류 : 수학, 분할 정복을 이용한 거듭제곱
# 피보나치 수 3에서 나눠지는 수만 달리진 문제
N = int(input()) - 1
li = [[1,1],[1,0]]
ans = [[1,0],[0,1]]
def cal(a,b) :
    res = [[0,0],[0,0]]
    for i in range(2) :
        for j in range(2) :
            for k in range(2) :
                res[i][j] = (res[i][j] + a[i][k]*b[k][j]) % 1000000007
    return res
while N :
    if N%2 :
        ans = cal(ans,li)
    li = cal(li,li)
    N //= 2
print(ans[0][0])