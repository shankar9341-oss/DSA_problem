class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        st = [stones[0]] * len(stones)
        for i in range(1, len(stones)):
            st[i] = st[i-1] + stones[i]

        dp = [0] * len(stones)
        dp[-1] = st[-1]
        for i in range(len(stones)-2, -1, -1):
            dp[i] = max(dp[i+1], st[i] - dp[i+1])

        return dp[1]