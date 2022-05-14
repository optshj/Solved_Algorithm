#2530번 인공지능 시계
#BRONZE 4
import sys

ho , mi , se = map(int,sys.stdin.readline().split())
need = int(input())
se += need
mi += se//60
ho += mi//60

if ho >= 24 :
    ho = ho%24

print(f'{ho} {mi%60} {se%60}')