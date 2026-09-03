class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) % 2:
            return True
        
        for n in nums1:
            if n % 2:
                return False
                break
        return True