# 백준 2580번 스도쿠
# GOLD 4
# 알고리즘 분류 : 백 트래킹
import sys
input = sys.stdin.readline
li = [list(map(int,input().split())) for _ in range(9)]
k = []
for i in range(9) :
    for j in range(9) :
        if li[i][j] == 0 :
            k.append([i,j])
def check(x,y,m) :
    for i in range(9) :
        if m == li[i][y] :
            return 0
    for i in range(9) :
        if m == li[x][i] :
            return 0
    for i in range((x//3)*3,(x//3)*3+3) :
        for j in range((y//3)*3,(y//3)*3+3) :
            if m == li[i][j] :
                return 0
    return 1

def dfs(start):
    if start >= len(k) :
        for i in li :
            print(*i)
        exit()
    for m in range(1,10):
        a,b = k[start]
        if check(a,b,m) :
            li[a][b] = m
            dfs(start+1)
            li[a][b] = 0
dfs(0)