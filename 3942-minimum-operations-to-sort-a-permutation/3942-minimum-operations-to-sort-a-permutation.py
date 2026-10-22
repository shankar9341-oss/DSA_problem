class Solution:
    def minOperations(self, nums: List[int]) -> int:
        drop_inc = 0
        drop_dec = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                drop_inc += 1
            else:
                drop_dec += 1
        
        if (
            (drop_inc > 1 or (drop_inc == 1 and nums[-1] > nums[0])) and
            (drop_dec > 1 or (drop_dec == 1 and nums[-1] < nums[0]))
        ): return -1

        if not drop_inc: return 0
        if not drop_dec: return 1

        if drop_inc == 1 and nums[-1] < nums[0]:
            for i in range(1, len(nums)):
                if nums[i] < nums[i -1]:
                    return min(i, len(nums) - i + 2)
        else:
            for i in range(1, len(nums)):
                if nums[i] > nums[i -1]:
                    return min(i, len(nums) - i) + 1

