class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if len(s) == 2:
            return -1

        minn, maxx = min(s) , max(s)
        if s[0] == minn or s[-1] == maxx:
            return 1
        for i in range(1, n-1):
            if s[i] == minn or s[i] == maxx:
                return 2
        return 3