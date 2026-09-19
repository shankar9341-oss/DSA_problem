class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(ans - target) > abs(total - target):
                    ans = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return ans


        
        
        
        
        
        
        
        
        
        
        
        # nums.sort()
        # closest = float("inf")

        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     left = i+1
        #     right = len(nums)-1

        #     while left < right:
        #         curr_sum = nums[i] + nums[left] + nums[right]
        #         if abs(curr_sum - target) < abs(closest - target):
        #             closest = curr_sum  
        #         if curr_sum > target:
        #             right -= 1
        #         elif curr_sum < target:
        #             left += 1
        #         else:
        #             return curr_sum

        # return closest
        
