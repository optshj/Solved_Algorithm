#2108번 통계학
#SILVER 3
import sys
from collections import Counter
a = int(sys.stdin.readline())
li = []
for i in range(a) :
    li.append(int(sys.stdin.readline()))
li.sort()
choi = Counter(li).most_common()
print(round(sum(li)/a))
print(li[(a-1)//2])
if len(choi) == 1 :
    print(choi[0][0])
else :
    if choi[0][1] == choi[1][1] :
        print(choi[1][0])
    else :
        print(choi[0][0])
print(max(li)-min(li))