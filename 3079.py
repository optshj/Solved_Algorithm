#3079번 입국심사
#GOLD 5
import sys
input_list = input().split()
N = int(input_list[0])
M = int(input_list[1])
data_time = []
time_max = 0
for i in range(N):
    input_list_2 = sys.stdin.readline().split()
    input_num = int(input_list_2[0])
    data_time.append(input_num)
    if input_num > time_max:
        time_max = input_num

left = 1
right = time_max * M
ans = right
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(N):
        cnt += mid // data_time[i]
    if cnt < M:                                 #mid 값 기준으로 계산하면 다 처리하기에 시간이 부족함;
        left = mid + 1
    else:                                       #mid 값 기준으로 계산하면 다 처리 가능; 정답의 후보가 됨
        right = mid - 1
        if mid < ans:
            ans = mid
print(ans)