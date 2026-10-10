class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        dif = []
        for i in range(n): dif.append(abs(nums1[i] - nums2[i]))
        m = max(dif)
        buckets = [0] * (m + 1)
        for d in dif: buckets[d] += 1

        k = k1 + k2
        for i in range(m , 0, -1):
            moves = min(buckets[i], k)
            buckets[i] -= moves
            buckets[i - 1] += moves
            k -= moves
            if k == 0: 
                break
        
        res = 0
        for i in range(m + 1): res += i ** 2 * buckets[i]
        
        return res