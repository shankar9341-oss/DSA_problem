class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        row = defaultdict(set)
        col = defaultdict(set)

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    row[i].add(j)
                    col[j].add(i)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and (len(row[i]) > 1 or len(col[j]) > 1):
                    res += 1

        return res