# 백준 10830번 행렬 제곱
# GOLD 4
# 알고리즘 분류 : 수학, 분할 정복, 분할 정복을 이용한 거듭제곱, 선형대수학
N,B = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
def cal(a,b) :
    res = [[0]*N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            for k in range(N) :
                res[i][j] += a[i][k]*b[k][j]
    for i in range(N) :
        for j in range(N) :
            res[i][j] %= 1000
    return res
        
def mul(B) :
    if B == 1 :
        return li
    m = mul(B//2)
    if B%2 : return cal(cal(m,m),li)
    else : return cal(m,m)
result = mul(B)
for i in range(N) :
    for j in range(N) :
        print(result[i][j]%1000,end = ' ')
    print()
