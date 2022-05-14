#1676번 팩토리얼 0의 개수
#SILVER 4
import sys
import math
N = int(sys.stdin.readline())
result = list(str(math.factorial(N)))
cnt = 0
result.reverse()
for i in result :
    if i == '0' :
        cnt += 1
    else :
        break
print(cnt)