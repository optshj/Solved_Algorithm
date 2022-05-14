#2798¹ø ºí·¢Àè
#BRONZE 2
import sys
N,M = map(int,sys.stdin.readline().split())
card = sorted(list(map(int,sys.stdin.readline().split())))
li = []
for i in range(0,N) :
    for f in range(i+1,N) :
        for k in range(f+1,N) :
            mini = card[i] + card[f] + card[k]
            if mini <= M :
                li.append(mini)
            else :
                pass
print(max(li))