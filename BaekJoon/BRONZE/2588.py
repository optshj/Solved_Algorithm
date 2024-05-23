#2588¹ø °ö¼À
#BRONZE 4
A = int(input())
B = int(input())
C = list(str(B))
for i in range(0,3):
    C[i] = int(C[i])
print(A*C[2])
print(A*C[1])
print(A*C[0])
print(A*B)