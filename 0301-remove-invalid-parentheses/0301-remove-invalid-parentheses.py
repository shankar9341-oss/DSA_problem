class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.res = []
        @cache
        def invalid(i, curr, d):
            if d < 0:
                return
            if i == len(s):
                if d == 0:
                    self.res.append(curr)
                return
            if s[i] not in "()":
                invalid(i + 1, curr + s[i], d)
            else:
                invalid(i + 1, curr + s[i], d + (1 if s[i] == "(" else -1))
                invalid(i + 1, curr, d)

        invalid(0, "", 0)
        maxx = max(len(st) for st in self.res)
        ans = [st for st in self.res if len(st) == maxx]
        
        return ans
