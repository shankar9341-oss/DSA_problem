class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        mp = {0:1}
        sum1 =  count = 0

        for i in range(len(nums)):
            sum1 += nums[i]
            count += mp.get(sum1 - k, 0)
            mp[sum1] = mp.get(sum1, 0) + 1

        return count


        
