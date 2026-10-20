MX = 10 ** 5 + 1
divisors = {n: [1, n] for n in range(1, MX)}
divisors[1] = [1]

for i in range(2, MX):
    for j in range(i * 2, MX, i):
        divisors[j].append(i)

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        def valid(d):
            prev_mx = 0
            for i in range(d, n +1, d):
                desc = -1
                for j in range(i - d, i -1):
                    if nums[j] > nums[j +1]:
                        if desc != -1: return False
                        else: desc = j + 1

                if desc != -1:
                    if nums [i - 1] > nums[i - d]:return False
                    mn, mx = nums[desc], nums[desc - 1]
                else: mn, mx = nums[i - d], nums [i - 1]

                if mn < prev_mx: return False
                prev_mx = mx
            return True

        n = len(nums)
        res = 0
        for d in divisors[n]:
            if  valid(d): res += d
        return res
