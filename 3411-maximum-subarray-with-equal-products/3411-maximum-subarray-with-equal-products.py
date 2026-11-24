class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            a = 1
            b = 0
            c = 1
            for j in range(i, len(nums)):
                a *= nums[j]
                b = gcd(b, nums[j])
                c = lcm(c, nums[j])
                if a == c * b:
                    res = max(res, j - i + 1)

        return res
