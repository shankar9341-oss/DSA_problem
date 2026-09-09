class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(1, len(nums), 2):
        #     if nums[i] != nums[i-1]:
        #         return nums[i-1]
        # return nums[len(nums)-1]
        result = 0
        for n in nums:
            result ^= n
        return result