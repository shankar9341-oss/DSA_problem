class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        if k == len(nums):
            return max(nums)
        
        if k == 1:
            ans = -1
            for n in nums:
                if count[n] == 1:
                    ans = max(ans, n)
            return ans

        ans = -1
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])

        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans









