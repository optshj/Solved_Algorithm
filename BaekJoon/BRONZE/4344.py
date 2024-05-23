#4344번 평균은 넘겠지
#BROZNE 1
import sys

a = int(input())
for i in range(a) :
    li = list(map(int,sys.stdin.readline().split()))
    result = 0
    cnt = 0
    for f in range(1,len(li)) :
        result += li[f]
    result = result/li[0]
    for f in range(1,len(li)) :
        if li[f] > result :
            cnt += 1
    print(f'{cnt/li[0]*100:.3f}%')