class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        grp = []
        num_grp = {}
        for n in sorted(nums):
            if not grp or abs(n - grp[-1][-1]) > limit:
                grp.append(deque())
            
            grp[-1].append(n)
            num_grp[n] = len(grp)-1

        res = []
        for n in nums:
            j = num_grp[n]
            res.append(grp[j].popleft())
        return res
