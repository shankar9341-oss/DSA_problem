class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[set() for _ in range(m)] for _ in range(n)]
        dp[0][0].add(grid[0][0])

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: continue
                curr = grid[i][j]
                cs = set()
                if i == 0:
                    for prev in dp[i][j - 1]:
                        cs.add(prev ^ curr)
                elif j == 0:
                    for prev in dp[i - 1][j]:
                        cs.add(prev ^ curr)
                else:
                    for prev in dp[i][j - 1]:
                        cs.add(prev ^ curr)
                    for prev in dp[i - 1][j]:
                        cs.add(prev ^ curr)
                dp[i][j] = cs

        return min(dp[-1][-1])

