#1620번 나는야 포켓몬 마스터 이다솜
#SILVER 4
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
li1 = {}
li2 = {}

for _ in range(1,N+1) :
    n = input().rstrip()
    li1[_] = n
    li2[n] = _

for _ in range(M) :
    m = input().rstrip()
    try :
        print(li1[int(m)])
    except :
        print(li2[m])