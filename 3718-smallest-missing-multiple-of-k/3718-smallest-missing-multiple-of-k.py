class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sett = set(nums)
        curr = k
        while curr in sett:
            curr += k
        return curr