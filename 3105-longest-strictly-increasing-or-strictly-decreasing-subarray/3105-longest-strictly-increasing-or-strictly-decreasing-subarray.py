class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr = 1
        res = 1
        incs = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if incs > 0:
                    curr += 1
                else:
                    curr = 2
                    incs = 1
            elif nums[i - 1] > nums[i]:
                if incs < 0:
                    curr += 1
                else:
                    curr = 2
                    incs = -1
            else:
                curr = 1
                incs = 0

            res = max(res, curr)
        
        return res
