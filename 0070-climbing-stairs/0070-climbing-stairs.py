class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        p2 = 1
        p1 = 2
        for i in range(3, n+1):
            curr = p1 + p2
            p1, p2 = curr, p1
        return p1