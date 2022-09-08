# 백준 1430번 공격
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 그래프 탐색, 기하학, 너비 우선 탐색
# 타워가 줄 수 있는 데미지는 2^자기깊이 만큼 관여할 수 있다.
from collections import deque
M = 1001
check = [[0]*M for _ in range(M)]
def distance(x1,y1,x2,y2) :
    if ((x1-x2)**2+(y1-y2)**2)**0.5 <= R :
        return True
    return False

def bfs() :
    q = deque()
    q.append([X,Y,0])
    check[Y][X] = 1
    ans = 0
    while q :
        x,y,v = q.popleft()
        if v :
            ans += D/(2**(v-1))
        for x_,y_ in top :
            if not distance(x,y,x_,y_) :
                continue
            if not check[y_][x_] :
                q.append([x_,y_,v+1])
                check[y_][x_] = 1
    return float(ans)
N,R,D,X,Y = map(int,input().split())
top = [list(map(int,input().split())) for _ in range(N)]
print(bfs())