import itertools
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        n = len(s)
        fm = defaultdict(int)
        for c in s: fm[c] += 1
        res = []

        for ti in range(n):
            t = target[ti]
            if fm[t] > 0:
                fm[t] -= 1
                largest = []
                for ci in range(25, -1, -1):
                    c = chr(ci + ord('a'))
                    if fm[c] > 0: largest.append(c * fm[c])
                if "".join(largest) > target[ti + 1:]:
                    res.append(t)
                    continue
                fm[t] += 1

            for nti in range(ord(t) - ord('a') +1, 26):
                c = chr(nti + ord('a'))
                if fm[c] > 0:
                    res.append(c)
                    fm[c] -= 1
                    smallest = []
                    for ci in range(26):
                        c = chr(ci + ord('a'))
                        if fm[c] > 0: smallest.append(c * fm[c])
                    return "".join(res + smallest)
            return ""

        return ""
