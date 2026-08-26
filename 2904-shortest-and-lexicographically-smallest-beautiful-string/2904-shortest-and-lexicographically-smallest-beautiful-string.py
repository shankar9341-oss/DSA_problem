class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # result = " "
        # left = 0
        # count = 0
        # for right in range(len(s)):
        #     if s[right] == "1": 
        #         count += 1
            
        #     # while left < right and (x > k or s[right] == "0"):
        #     while count > k:
        #         if s[left] == "1":
        #             left -= 1
        #         left += 1

        #     if count == k:
        #         s1 = s[left:right + 1]
        #         if not result or len(s1) < len(result) or (len(s1) == len(result) and s1 < result):
        #             result = s1
        # return result

        n = len(s)
        res = ''
        x = 0
        l = 0
        for r in range(n):
            if s[r] == '1': x += 1
            while l < r and (x > k or s[l] == '0'):
                if s[l] == '1': x -= 1
                l += 1
            if x == k:
                ss = s[l : r+1]
                if not res or len(ss) < len(res) or (len(ss) == len(res) and ss < res):
                    res = ss

        return res