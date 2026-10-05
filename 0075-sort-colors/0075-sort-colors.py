class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        idx = 0
        def swapping(idx, j):
            nums[idx], nums[j] = nums[j], nums[idx]

        while idx <= right:
            if nums[idx] == 0:
                swapping(left, idx)
                left += 1
            elif nums[idx] == 2:
                swapping(idx, right)
                right -= 1
                idx -= 1
            idx += 1
