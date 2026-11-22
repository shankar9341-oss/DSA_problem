class Solution:
    def checkString(self, s: str) -> bool:
        seen = False
        for char in s:
            if char == "b":
                seen = True
            elif char == "a" and seen:
                return False
        return True