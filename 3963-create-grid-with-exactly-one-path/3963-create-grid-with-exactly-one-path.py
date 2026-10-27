class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [["#"] * n for _ in range(m)]
        
        for i in range(m):
            res[i][0] = "."
        for j in range(n):
            res[-1][j] = "."

        return["".join(row) for row in res]