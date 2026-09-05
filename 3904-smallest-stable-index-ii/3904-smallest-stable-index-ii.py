class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix = [nums[0]] * len(nums)
        sufix = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = max(prefix[i-1], nums[i])

        for i in range(len(nums)-2, -1, -1):
            sufix[i] = min(sufix[i+1], nums[i])

        for i in range(len(nums)):
            if prefix[i] - sufix[i] <= k:
                return i
        
        return -1
