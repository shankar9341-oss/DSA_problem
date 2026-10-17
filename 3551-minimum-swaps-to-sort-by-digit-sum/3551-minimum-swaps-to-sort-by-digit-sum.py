class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        initial = {n : i for i,n in enumerate(nums)}

        def digitsum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        nums.sort()
        nums.sort(key = lambda x: digitsum(x))

        res = 0
        sett = set()
        for i in range(len(nums)):
            if i in sett:
                continue
            
            j = i
            step = 0
            while not j in sett:
                sett.add(j)
                step += 1
                j = initial[nums[j]]

            res += step - 1

        return res