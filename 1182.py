#1182번 부분수열의 합
#SILVER 2
import sys
input = sys.stdin.readline
N , S = map(int,input().split())
li = sorted(list(map(int,input().split())))
k = []
global result
result = 0
def dfs(start):
    global result
    for i in range(start,N):
        k.append(li[i])
        if sum(k) == S :
            result += 1
        dfs(i+1)
        k.pop()
dfs(0)
print(result)