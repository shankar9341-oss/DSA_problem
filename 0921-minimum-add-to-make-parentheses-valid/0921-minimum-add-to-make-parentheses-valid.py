class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openn = 0
        closee = 0
        for char in s:
            if char == "(":
                openn += 1
            else:
                if openn > 0:
                    openn -= 1
                else:
                    closee += 1
        
        return openn + closee
