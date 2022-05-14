#1181번 단어 정렬
#SILVER 5
import sys
a = int(sys.stdin.readline())
li = []
for f in range(a) :
    word = str(sys.stdin.readline())
    li.append(word)
li = list(set(li))
li1 = []
for i in li :
    li1.append([len(i),i])
li1.sort()
for f in li1 :
    print(f[1],end='')