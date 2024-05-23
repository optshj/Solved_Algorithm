#3009번 네 번째 점
#BROZNE 3
A = []
B = []

for i in range(3):
    X , Y = map(int,input().split())
    A.append(X)
    B.append(Y)
A = sorted(A)
B = sorted(B)
if A.count(A[0]) == 1 and B.count(B[0]) == 1 :
    print(f'{A[0]} {B[0]}')

elif A.count(A[0]) == 1 and B.count(B[2]) == 1 :
    print(f'{A[0]} {B[2]}')

elif A.count(A[2]) == 1 and B.count(B[0]) == 1 :
    print(f'{A[2]} {B[0]}')

elif A.count(A[2]) == 1 and B.count(B[2]) == 1 :
    print(f'{A[2]} {B[2]}')