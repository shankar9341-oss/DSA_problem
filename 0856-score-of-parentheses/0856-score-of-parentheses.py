class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                score += 1
            else:
                score -= 1
                if s[i-1] == "(":
                    count += 1 << score

        return count            