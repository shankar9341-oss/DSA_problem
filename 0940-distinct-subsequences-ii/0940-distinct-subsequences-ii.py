class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ch = 10 ** 9 + 7
        f = [0] * 26
        for char in s:
            f[ord(char) - ord("a")] = 1 + sum(f) % ch
        
        return sum(f) % ch