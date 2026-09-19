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


        
        
        
        
        
        
        
        
