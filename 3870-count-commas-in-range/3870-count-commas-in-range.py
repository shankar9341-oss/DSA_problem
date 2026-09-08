class Solution:
    def countCommas(self, n: int) -> int:
        if n < 999:
            return 0
        count = 0
        for _ in range(1000, n+1):
            count += 1
        return count
        
        
        
        
        
        
        # if n < 999:
        #     return 0
        # else:
        #     return max(n - 999, 0)