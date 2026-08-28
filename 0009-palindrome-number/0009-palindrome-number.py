class Solution:
    def isPalindrome(self, x: int) -> bool:

        temp = x
        result = 0
        while temp > 0:
            rev = temp % 10
            temp //= 10
            result = result * 10 + rev
        return result == x

          
        