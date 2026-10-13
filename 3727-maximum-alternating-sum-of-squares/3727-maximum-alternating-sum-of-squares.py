class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(num) for num in nums]
        nums.sort(reverse = True)
        even = sum(num ** 2 for num in nums[:ceil(len(nums)/2)])
        odd = sum(num ** 2 for num in nums[ceil(len(nums)/2):])

        return even - odd