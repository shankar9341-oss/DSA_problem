class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = max_count = 0
    
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 0

        return max(max_count,curr_count)
