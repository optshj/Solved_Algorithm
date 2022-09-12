# 백준 1647번 도시 분할 계획
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 최소 스패닝 트리
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
g = []
union = [i for i in range(N+1)]
def find(v) :
    if v != union[v] :
        union[v] = find(union[v])
    return union[v]
ans = 0
val = 0
for i in range(M) :
    a,b,c = map(int,input().split())
    if a > b :
        a,b = b,a
    g.append([c,a,b])
g.sort()
for c,a,b in g :
    s = find(a)
    e = find(b)
    if s != e :
        if s > e :
            union[s] = e
        else :
            union[e] = s
        ans += c
        val = max(val,c)
print(ans-val)