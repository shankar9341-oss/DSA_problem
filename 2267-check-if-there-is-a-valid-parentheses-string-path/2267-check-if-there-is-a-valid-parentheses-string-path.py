class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        st = len(grid)
        end = len(grid[0])
        @cache
        def dp(i,j,bal):
            if i == st - 1 and j == end - 1:
                return bal == 0
            if bal < 0:
                return False
            
            if(
                i + 1 < st and 
                dp(i + 1, j, bal + 1 if grid[i + 1][j] == "(" else bal - 1)
            ): return True

            if(
                j + 1 < end and 
                dp(i, j + 1, bal + 1 if grid[i][j + 1] == "(" else bal - 1)
            ): return True

            return False

        return dp(0,0,1 if grid[0][0] == "(" else -1)