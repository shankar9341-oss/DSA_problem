class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = 0
        ans = False
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            if not ans:
                res = nums[i]
                ans = True
            else:
                res &= nums[i]

        return res