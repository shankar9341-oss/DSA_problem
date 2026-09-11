class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        sett = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i in (j,k) or j in (i,k) or digits[i] == 0 or digits[k] % 2 == 1:
                        continue
                    res = (digits[i] * 100) + (digits[j] * 10) + digits[k]
                    sett.add(res)
        return len(sett)