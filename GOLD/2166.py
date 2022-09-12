# 백준 2166번 다각형의 면적
# GOLD 5
# 알고리즘 분류 : 기하학, 다각형의 넓이
# 신발끈 공식을 이용하면 풀 수 있다.
import sys
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
li.append(li[0])
ans = 0
for i in range(N) :
    ans += li[i][0] * li[i+1][1]
    ans -= li[i][1] * li[i+1][0]
ans = abs(ans*0.5)
print(ans)