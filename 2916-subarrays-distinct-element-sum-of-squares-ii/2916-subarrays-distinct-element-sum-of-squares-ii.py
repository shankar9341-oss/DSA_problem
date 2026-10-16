
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        cnt, tot = [0] * (n + 1), [0] * (n + 1) 
        last, ans = {}, 0
        for r, x in enumerate(nums):
            p = last.get(x, -1)
            c = s = 0
            i = n - p - 1  
            while i:
                c += cnt[i]
                s += tot[i]
                i -= i & -i
            ans += (n - r) * ((r - p) ** 2 - 2 * (s - p * c))
            i = n - p  
            while i <= n:
                cnt[i] += 1
                tot[i] += p
                i += i & -i
            last[x] = r
        return ans % (10**9 + 7)