class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for idx,ele in enumerate(nums):
            result = 0

            while ele:
                result += ele % 10
                ele //= 10

            if idx == result:
                return idx
                
        return -1
