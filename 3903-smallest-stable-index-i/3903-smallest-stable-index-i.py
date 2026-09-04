class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        for i in range(len(nums)):
            maxx = -inf
            minn = inf
            for j in range(i + 1):
                maxx = max(maxx, nums[j])
            for j in range(i, len(nums)):
                minn = min(minn, nums[j])
            if maxx - minn <= k:
                return i
        return -1           
