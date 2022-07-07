# 백준 2749번 피보나치 수 6
# GOLD 2
# 알고리즘 분류 : 수학, 분할 정복을 이용한 거듭제곱
# 피보나치 수를 행렬로 표현할 수 있음.
# [[F n+2],[F n+1]] = [[1,1],[1,0]] X [[F n+1],[F n]]
# 처음에 재귀를 이용해 배열의 거듭제곱을 구현 -> 메모리 초과
# 반복문으로 거듭제곱을 구현함.
# 파사노주기를 이용하여 구할 수 있음. 파사노주기 이해 못함.
N = int(input()) - 1
li = [[1,1],[1,0]]
ans = [[1,0],[0,1]]
def cal(a,b) :
    res = [[0,0],[0,0]]
    for i in range(2) :
        for j in range(2) :
            for k in range(2) :
                res[i][j] = (res[i][j] + a[i][k]*b[k][j]) % 1000000
    return res
while N :
    if N%2 :
        ans = cal(ans,li)
    li = cal(li,li)
    N //= 2
print(ans[0][0])

# 파사노 주기를 이용한 풀이
a,b = 0,1
n = int(input())
# 주기 공식 10^n으로 나눈 나머지의 피사노 주기 = 15*10^(n-1)
# 100만은 10^6 피사노 주기는 15*10^5
n = n % 1500000

for i in range(n):
    a,b = b%1000000, (a+b)%1000000

print(a)