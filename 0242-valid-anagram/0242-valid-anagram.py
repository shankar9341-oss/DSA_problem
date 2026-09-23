class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)
        
        
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)