class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            res = 0
            while n:
                res += n % 10
                n //= 10
            if res == i:
                return i
        return -1                