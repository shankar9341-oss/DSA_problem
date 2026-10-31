class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(grid)
        m = len(grid[0])
        dp = [[[0,0] for _ in range(m)]for _ in range(n)]

        for i in range(1,n):
            dp[i][0] = [0,1]
            if grid[i][0] == 1:
                break

        for j in range(1,m):
            dp[0][j] = [1,0]
            if grid[0][j] == 1:
                break

        for i in range(1,n):
            for j in range(1,m):
                if grid[i - 1][j] == 0:
                    dp[i] [j][1] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                else:
                    dp[i] [j][1] = dp[i - 1][j][0]

                if grid[i][j - 1] == 0:
                    dp[i][j][0] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                else:
                    dp[i][j][0] = dp[i][j - 1][1]

        return (dp[-1][-1][0] + dp[-1][-1][1]) % MOD
