class Solution:
    def checkValidString(self, s: str) -> bool:
        left_max, left_min = 0, 0
        for char in s:
            if char == "(":
                left_min = left_min + 1
                left_max = left_max + 1
            elif char == ")":
                left_min = left_min - 1
                left_max = left_max - 1
            else:
                left_min = left_min - 1
                left_max = left_max + 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        
        return left_min == 0