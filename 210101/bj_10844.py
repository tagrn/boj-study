from sys import stdin
input = stdin.readline


N = int(input())
dp = [[0] * 10 for i in range(100)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    for j in range(10):
        if 0 < j < 9:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        elif j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        else:
            dp[i][j] = dp[i - 1][j - 1]

print(sum(dp[N-1])%1000000000)