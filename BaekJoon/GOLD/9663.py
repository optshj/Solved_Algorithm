#9663번 N-Queen
#GOLD 5
import sys
N = int(sys.stdin.readline())

ans = 0
li = [0]*N

def check(q):
    for i in range(q):
        if li[q]==li[i]:
            return False
        elif abs(li[q]-li[i]) == q-i:
            return False
    return True

def dfs(q):
    global ans
    if q == N :
        ans += 1
        return

    for i in range(N):
        li[q] = i
        if check(q) :
            dfs(q+1)


dfs(0)
print(ans)