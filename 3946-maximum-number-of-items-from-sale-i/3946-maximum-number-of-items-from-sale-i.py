class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0: bonus[i] += 1

        dp = [[0] * (budget + 1) for _ in range(n)]
        for j in range(items[0][1], budget + 1): dp[0][j] = j // items[0][1] + bonus[0]

        for i in range(1, n):
            f, p = items[i]
            for j in range(budget + 1):
                dp[i][j] = dp[i - 1][j]
                if p > j: continue
                dp[i][j] = max(dp[i][j], dp[i - 1][j - p] + bonus[i] + 1, dp[i][j - p] + 1)

        return dp[-1][-1]