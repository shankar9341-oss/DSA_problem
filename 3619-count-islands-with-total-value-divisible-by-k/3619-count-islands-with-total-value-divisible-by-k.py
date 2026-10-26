class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n,m = len(grid),len(grid[0])

        def dfs(i,j):
            if i < 0 or i == n or j < 0 or j == m or grid[i][j] == 0 or (i,j) in sett:
                return 0
            sett.add((i,j))
            total = grid[i][j]

            for ni,nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                total += dfs(ni,nj)
            return total

        res = 0
        sett = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 or (i,j) in sett:
                    continue
                if dfs(i,j) % k == 0:
                    res += 1

        return res
