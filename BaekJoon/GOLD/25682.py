# 백준 25682번 체스판 다시 칠하기 2
# GOLD 5
# 알고리즘 분류 : 누적 합
import sys
input = sys.stdin.readline

def chess(color):
    li = [[0] * (M + 1) for _ in range(N + 1)]
    cnt = sys.maxsize
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0: 
                val = board[i][j] != color
            else:
                val = board[i][j] == color
            li[i + 1][j + 1] = li[i][j + 1] + li[i + 1][j] - li[i][j] + val
    
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            cnt = min(cnt, li[i + K - 1][j + K - 1] - li[i + K - 1][j - 1] - li[i - 1][j + K - 1] + li[i - 1][j - 1])
    return cnt

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
print(min(chess('B'), chess('W')))