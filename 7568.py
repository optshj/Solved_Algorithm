#7568¹ø µ¢Ä¡
#SILVER 5
import sys
N = int(sys.stdin.readline())
weight = []
high = []
rank = [1]*N

for i in range(N) :
    W , H = map(int,sys.stdin.readline().split())
    weight.append(W)
    high.append(H)

for f in range(0,N) :
    cnt = 0
    for k in range(f+1,N) :
        if weight[f] > weight[k] and high[f] > high[k] :
            rank[k] += 1

        elif weight[f] < weight[k] and high[f] < high[k] :
            rank[f] +=1 

for i in rank :
    print(i,end = ' ')