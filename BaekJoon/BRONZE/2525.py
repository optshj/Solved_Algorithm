#2525�� ���� �ð�
#BRONZE 4
M,N = map(int,input().split())
need = int(input())
print(f'{(M + (N + need)//60)%24} {(N + need)%60 }')