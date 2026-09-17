class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        res = inf
        ans = 0
        st = [inf] * len(arr)
        left = 0
        for right in range(len(arr)):
            ans += arr[right]
            while ans > target:
                ans -= arr[left]
                left += 1
            
            st[right] = st[right - 1] if right - 1 >= 0 else inf
            if ans == target:
                res = min(res, right - left + 1 + (st[left - 1] if left - 1 >= 0 else inf))

                st[right] = min(st[right], right - left + 1)

        return -1 if res == inf else res

