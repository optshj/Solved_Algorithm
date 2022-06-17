# 백준 1051번 숫자 정사각형
# SILVER 4
# 알고리즘 분류 : 구현, 브루트포스 알고리즘 
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
li = [list(map(str,input())) for _ in range(N)]
ans = 1
for i in range(N) :
    for j in range(M) :
        for gap in range(1,min(N-i,M-j)) :
            if li[i][j] == li[i+gap][j] and li[i][j] == li[i][j+gap] and li[i][j] == li[i+gap][j+gap] :
                if ans < (gap+1)**2 :
                    ans = (gap+1)**2
print(ans)