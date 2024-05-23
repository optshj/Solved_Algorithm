# 백준 1525번 퍼즐
# GOLD 2
# 알고리즘 분류 : 그래프 이론, 자료 구조, 그래프 탐색, 너비 우선 탐색
# 메모리 제한때문에 check를 사전형으로 구현함
from collections import deque
li = [list(map(int,input().split())) for _ in range(3)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
check = {}
val = []
for i in range(3) :
    for j in range(3) :
        if li[i][j] == 0 :
            val.append('9')
        else :
            val.append(str(li[i][j]))
q = deque()
q.append(''.join(val))
check[''.join(val)] = 0
def bfs() :
    while q :
        a = q.popleft()
        if a == '123456789' :
            return check[a]
        lo = a.find('9')
        x = lo%3
        y = lo//3
        for i in range(4) :
            x_ = x + dx[i]
            y_ = y + dy[i]
            if x_ < 0 or x_ > 2 or y_ < 0 or y_ > 2 :
                continue
            k = list(a)
            k[x_+y_*3],k[lo] = k[lo],k[x_+y_*3]
            b = ''.join(k)
            try :
                check[b]
            except :
                check[b] = check[a] + 1
                q.append(b)
    return -1
print(bfs())