# 백준 23842번 성냥개비
# SILVER 4
# 알고리즘 분류 : 브루트포스 알고리즘
li = [6,2,5,5,4,5,6,3,7,6]
N = int(input()) - 4
for i in range(100) :
    for j in range(100-i) :
        c = i + j
        a_cnt = li[i//10] + li[i%10]
        b_cnt = li[j//10] + li[j%10]
        c_cnt = li[c//10] + li[c%10]
        if a_cnt + b_cnt + c_cnt == N :
            print(f"{i//10}{i%10}+{j//10}{j%10}={c//10}{c%10}")
            exit()
print('impossible')