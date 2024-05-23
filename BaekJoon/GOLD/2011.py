# 백준 2011번 암호코드
# GOLD 5
# 알고리즘 분류 : 다이나믹 프로그래밍
word = [0]+ list(map(int,input()))
dp = [0]*(len(word))
dp[0] = 1
for i in range(1,len(word)) :
  if word[i] == 0 :
    if word[i-1] != 1 and word[i-1] != 2 :
      print(0)
      exit()
  else :
    dp[i] += dp[i-1]%1000000
  if 10 <= word[i-1]*10 + word[i] <= 26 :
    dp[i] += dp[i-2]%1000000
print(dp[-1]%1000000)