#2525¹ø ¿Àºì ½Ã°è
#BRONZE 4
M,N = map(int,input().split())
need = int(input())
print(f'{(M + (N + need)//60)%24} {(N + need)%60 }')