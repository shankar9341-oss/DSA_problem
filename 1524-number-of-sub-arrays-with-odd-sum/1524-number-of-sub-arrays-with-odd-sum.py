class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        p1 = 0
        s1 = 0
        r1 = 1
        res = 0
        for n in arr:
            p1 += n

            if p1 % 2 == 0:
                res += s1
                r1 += 1
            else:
                res += r1
                s1 += 1

        return res % (10**9 + 7)