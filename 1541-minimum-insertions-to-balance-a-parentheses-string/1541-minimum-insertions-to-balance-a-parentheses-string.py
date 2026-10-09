class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        res = 0 
        for char in s:
            if char == "(":
                count += 2
                if count % 2 == 1:
                    res += 1
                    count -= 1
            else:
                count -= 1
                if count < 0:
                    res += 1
                    count = 1
        
        return res + count
