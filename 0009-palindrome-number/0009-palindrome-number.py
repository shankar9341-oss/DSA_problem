class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        res = 0
        while temp > 0:
            n = temp % 10
            temp //= 10
            res = res * 10 + n
        return res == x
          
        