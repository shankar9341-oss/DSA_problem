class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        curr = 0
        res = []
        for char in seq:
            if char == "(":
                res.append(curr % 2)
                curr += 1
            else:
                curr -= 1
                res.append(curr % 2)

        return res