# 백준 4386번 별자리 만들기
# GOLD 3
# 알고리즘 분류 : 그래프 이론, 최소 스패닝 트리
import sys

input = sys.stdin.readline
N = int(input())
li = [list(map(float, input().split())) for _ in range(N)]
g = []
union = [i for i in range(N + 1)]
ans = 0


def find(v):
    if v != union[v]:
        union[v] = find(union[v])
    return union[v]


def length(a, b):
    return (abs(li[a][0] - li[b][0])**2 + abs(li[a][1] - li[b][1])**2)**0.5


for i in range(N):
    for j in range(i + 1, N):
        g.append([length(i, j), i + 1, j + 1])

g.sort()
for v, i, j in g:
    s = find(i)
    e = find(j)
    if s != e:
        if s > e:
            union[s] = e
        else:
            union[e] = s
        ans += v
print(f'{ans:.2f}')