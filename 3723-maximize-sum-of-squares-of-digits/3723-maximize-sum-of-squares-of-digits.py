class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = '9' * (sum // 9)
        sum %= 9
        if sum:
            res += str(sum)

        r = len(res)
        if r > num:
            return ''

        res += '0' * (num - r)

        return res