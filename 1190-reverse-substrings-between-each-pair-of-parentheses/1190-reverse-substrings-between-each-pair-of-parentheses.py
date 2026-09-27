class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        for char in s:
            if char == ")":
                curr = []
                while res and res[-1] != "(":
                    curr.append(res.pop())
                res.pop()
                res += curr
            else:
                res.append(char)

        return "".join(res)
