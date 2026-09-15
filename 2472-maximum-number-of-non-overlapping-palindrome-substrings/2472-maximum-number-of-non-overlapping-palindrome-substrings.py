class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        is_palindrome = [[False] * len(s) for _ in range(len(s))]
        for l in range(1, len(s) + 1):
            for left in range(len(s) - l + 1):
                right = left + l - 1
                is_palindrome[left][right] = s[left] == s[right] and (l <= 2 or is_palindrome[left + 1] [right - 1])

        res = [0] * len(s)
        for i in range(len(s)):
            if i > 0:
                res[i] = res[i - 1]
            for j in range(i - k + 2):
                if is_palindrome[j][i]:
                    prev = res[j - 1] if j - 1 >= 0 else 0
                    res[i] = max(res[i], prev + 1)
        return res[len(s) - 1]


