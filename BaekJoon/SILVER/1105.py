# 백준 1105번 팔
# SILVER 1
# 알고리즘 분류 : 수학, 그리디 알고리즘
L,R = map(str,input().split())
cnt = 0
if len(L) != len(R) :
    print(0)
else :
    for i in range(len(L)) :
        if L[i] == '8' and R[i] == '8' :
            cnt += 1
        elif L[i] == R[i] :
            pass
        else :
            break
    print(cnt)