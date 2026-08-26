class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        result = ''
        left = 0
        count = 0
        for right in range(len(s)):
            if s[right] == "1": 
                count += 1
            
            while left < right and (count > k or s[left] == "0"):
                if s[left] == "1": 
                    count -= 1
                left += 1

            if count == k:
                s1 = s[left:right + 1]
                if not result or len(s1) < len(result) or (len(s1) == len(result) and s1 < result):
                    result = s1
        return result

     