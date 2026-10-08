class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0
        for char in s:
            count += 1 if char == "(" else -1
            if (char == "(" and count == 1) or (char == ")" and count == 0): 
                continue
            res.append(char)

        return "".join(res)