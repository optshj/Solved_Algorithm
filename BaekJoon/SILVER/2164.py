#2164�� ī��2
#SILVER 4
from collections import deque

a = int(input())
li = deque(list(range(1,a+1)))
while True :
    if len(li) == 1:
        break
    li.popleft()
    li.append(li.popleft())
print(li[0])