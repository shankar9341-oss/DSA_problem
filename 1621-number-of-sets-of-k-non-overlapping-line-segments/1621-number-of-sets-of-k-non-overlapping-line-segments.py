class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n + k - 1 ,k * 2) % (10 ** 9 + 7)