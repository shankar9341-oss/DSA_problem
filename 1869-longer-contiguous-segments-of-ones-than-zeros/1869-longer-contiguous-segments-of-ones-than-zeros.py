class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = 0
        max_zeros = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                if s[i-1] == '1':
                    max_ones = max(max_ones, count)
                else:
                    max_zeros = max(max_zeros, count)
                count = 1
        if s[-1] == '1':
            max_ones = max(max_ones, count)
        else:
            max_zeros = max(max_zeros, count)

        return max_ones > max_zeros