#1406번 에디터
#SILVER 2
import sys
a = list(str(sys.stdin.readline()))
a.pop()
b = int(sys.stdin.readline())
c = []
for i in range(b):
    k = list(sys.stdin.readline().split())
    if k[0] == 'P':
        a.append(k[1])

    elif k[0] == 'L':
        if a:
            c.append(a.pop())
        else :
            pass

    elif k[0] == 'D':
        if c:
            a.append(c.pop())
        else :
            pass
    else:
        if a:
            a.pop()
print(''.join(a+list(reversed(c))))