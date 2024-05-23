#5073번 삼각형과 세 변
#BROZNE 3
import sys
while True :
    li = sorted(list(map(int,sys.stdin.readline().split())))
    
    if sum(li) == 0 :
        break

    if li[2] >= li[1] + li[0] :
        print("Invalid")
    elif li[0] == li[2] :
        print("Equilateral")
    elif li[0] < li[1] and li[1] < li[2] :
        print("Scalene")
    else :
        print("Isosceles")