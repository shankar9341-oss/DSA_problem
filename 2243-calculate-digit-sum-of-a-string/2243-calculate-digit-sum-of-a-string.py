class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            curr = []
            for i in range(0,len(s),k):
                total = 0
                for j in range(i, min(i + k, len(s))):
                    total += int(s[j])
                curr.append(str(total))
            s = "".join(curr)

        return s