class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        max_sum = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]

            if curr > max_sum:
                max_sum = curr
        
        return max_sum / k
            


