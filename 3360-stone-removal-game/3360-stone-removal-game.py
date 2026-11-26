class Solution:
    def canAliceWin(self, n: int) -> bool:
        st = 10
        t = "a"
        while st <= n:
            if t == "a":
                t = "b"
            else:
                t = "a"
            n -= st
            st -= 1

        return t == "b"