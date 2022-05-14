#1018번 체스판 다시 칠하기
#SILVER 5
import sys
li = []
N , M = map(int,sys.stdin.readline().split())
b_res= []
w_res = []
for i in range(N) :
    A = str(sys.stdin.readline())
    li.append(A)

for j in range(0,N-7) :
    for k in range(0,M-7) :
        result = 0
        if li[j][k] == 'B' :
            for v in range(8) :
                for h in range(8) :
                    if (v+h)%2 == 0 and li[j+v][k+h] != 'B' :
                        result += 1
                    elif (v+h)%2 == 1 and li[j+v][k+h] != 'W' :
                        result += 1

        elif li[j][k] == 'W' :
            for v in range(8) :
                for h in range(8) :
                    if (v+h)%2 == 0 and li[j+v][k+h] != 'W' :
                        result += 1
                    elif (v+h)%2 == 1 and li[j+v][k+h] != 'B' :
                        result += 1
        w_res.append(result)
        b_res.append(64-result)
print(min(min(w_res),min(b_res)))