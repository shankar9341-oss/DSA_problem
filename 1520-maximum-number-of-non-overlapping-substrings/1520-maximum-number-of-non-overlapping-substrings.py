class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        interval = {}
        for i,e in enumerate(s):
            if not e in interval: interval[e] = [i,i]
            else: interval[e][1] = i
        
        for e in interval:
            left, right = interval[e]
            while True:
                l_copy, r_copy = left, right
                for i in range(l_copy, r_copy + 1):
                    left = min(left, interval[s[i]][0])
                    right = max(right, interval[s[i]][1])
                
                if (l_copy == left) and (r_copy == right):
                    break
            
            interval[e] = (left, right)

        cand = sorted(interval.values(), key = lambda x: x[1])
        res = []
        prev = -1

        for start, end in cand:
            if start > prev:
                res.append(s[start: end + 1])
                prev = end

        return res
