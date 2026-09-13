class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prod1 = 1
        for i in range(len(nums)):
            res[i] = prod1
            prod1 *= nums[i]

        prod2 = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prod2
            prod2 *= nums[i]

        return res
                
            

        # res = [0] * len(nums)
        # res[0] = 1
        # for i in range(1, len(nums)):
        #     res[i] = res[i-1] * nums[i-1]

        # right_prod = 1
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] *= right_prod
        #     right_prod *= nums[i]

        # return res

