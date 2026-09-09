class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        for i in range(1, 6):
            ans += max(0, n - (1000**i - 1))
        return ans