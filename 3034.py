#3034번 앵그리 창영
#BRONZE 3
import sys
input = sys.stdin.readline
N,W,H = map(int,input().split())
for _ in range(N) :
    if int(input()) > (W**2+H**2)**0.5 :
        print("NE")
    else :
        print("DA")