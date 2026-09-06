class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}
        for i,n in enumerate(nums):
            total = target - n
            if total in map:
                return [map[total], i]
            map[n] = i








                
        
                
        
