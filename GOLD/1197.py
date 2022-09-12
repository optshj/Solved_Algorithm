# 백준 1197번 최소 스패닝 트리
# GOLD 4
# 알고리즘 분류 : 그래프 이론, 최소 스패닝 트리
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
g = []
union = [i for i in range(V+1)]
def find(v) :
    if v != union[v] :
        union[v] = find(union[v])
    return union[v]
ans = 0
for i in range(E) :
    a,b,w = map(int,input().split())
    g.append([w,a,b])
g.sort()
for w,a,b in g :
    s = find(a)
    e = find(b)
    if s != e :
        if s > e :
            union[s] = e
        else :
            union[e] = s
        ans += w
print(ans)