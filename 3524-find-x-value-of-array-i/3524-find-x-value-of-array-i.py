class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [[0] * k for _ in range(len(nums))]

        for i in range(len(nums)):
            ans[i][nums[i] % k] += 1
            if i == 0:
                continue
            for j in range(k):
                ans[i][(j * nums[i]) % k] += ans[i-1][j]

        res = [0] * k
        for i in range(len(nums)):
            for j in range(k):
                res[j] += ans[i][j]

        return res