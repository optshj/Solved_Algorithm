#5430번 AC
#GOLD 5
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = list(str(input()))
    n = int(input())
    result = deque(map(str,input().rstrip()[1:-1].split(',')))
    if n == 0 :
        result = deque()
    R_cnt = 0
    c = 0
    for i in p:
        if i == 'R':
            R_cnt += 1
        elif i == 'D':
            if len(result)>0 :
                if R_cnt%2 == 1:
                    result.pop()
                else :
                    result.popleft()
            else :
                c = 1
                break
    if c == 1:
        print('error')
        continue

    if R_cnt%2 == 1:
        result.reverse()
        print("["+",".join(result)+"]")
    else :
        print("["+",".join(result)+"]")