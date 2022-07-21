# 백준 1041번 주사위
# GOLD 5
# 알고리즘 분류 : 수학, 그리디 알고리즘
N = int(input())
li = list(map(int,input().split()))
if N == 1 :
    print(sum(li) - max(li))
    exit()
side_2_li = []
side_3_li = []
for i in range(6) :
    for j in range(6) :
        if i + j == 5 or i == j:
            continue
        for k in range(6) :
            if i + k == 5 or j == k or j + k == 5 or i == k:
                continue
            side_3_li.append(li[i]+li[j]+li[k])
        side_2_li.append(li[i]+li[j])
side_1 = (N-2)**2 + 4*(N-2)*(N-1)
side_2 = 8*N - 4*3
side_3 = 4
print(side_3*(min(side_3_li)) + side_2*(min(side_2_li)) + side_1*(min(li)))

# 다른풀이
N = int(input())
A,B,C,D,E,F = map(int,input().split())
li = [A,B,C,D,E,F]
a = min(li)
b = min(A+B,A+C,A+D,A+E,B+C,B+D,B+F,C+E,C+F,D+E,D+F,E+F)
c = min(B+C+F,B+D+F,D+E+F,C+E+F,A+C+E,A+B+C,A+D+E,A+B+D)
if N == 1 :
    print(sum(li) - max(li))
else :
    side_1 = (N-2)**2 + 4*(N-2)*(N-1)
    side_2 = 8*N - 4*3 
    side_3 = 4
    print(side_3*c + side_2*b + side_1*a)