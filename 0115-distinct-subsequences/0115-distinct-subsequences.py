class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mapp = {}
        def dfs(i, j):
            if j == len(t): return 1
            if i == len(s): return 0
            if (i,j) in mapp: return mapp[(i,j)]
            
            if s[i] == t[j]:
                mapp[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                mapp[(i,j)] = dfs(i + 1, j)

            return mapp[(i,j)]

        return dfs(0, 0)