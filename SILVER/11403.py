# 백준 11403번 경로 찾기
# SILVER 1
# 알고리즘 분류 : 그래프, 플로이드-워셜
# 플로이드 알고리즘으로 방문하는것을 확인하면 되는 문제
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if li[i][j] == 1 or (li[i][k] == 1 and li[k][j] == 1 ):
                li[i][j] = 1
for i in li :
    print(*i)