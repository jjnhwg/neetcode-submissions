class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 1, 2, 4, 6
        # 1, 1, 2, 8
        #.48  24  6   1


        prefix = 1 
        res = [1] * len(nums)
        
        for i in range(len(nums)):
            res[i] = prefix 
            prefix = nums[i] * prefix
        
        
        postfix = 1
        for i in range(len(nums) -1 , -1, -1):
            res[i] = res[i] * postfix
            postfix = nums[i] * postfix
        return res





        