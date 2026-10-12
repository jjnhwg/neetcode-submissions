class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
        input array of nums
        output : array of nums that are multiplied with each other exepcet for the elemnt/index of the array
        that we are on
        '''


        prefix = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            prefix[i] = pre
            pre = nums[i] * pre


        #[1,2,4,6]

        #[1,1,2,8]
        #[48,24,6,1]

        #[48,24,12,8]

        res = [1] * len(nums)

        post = 1 

        for i in range(len(nums) - 1, -1, -1):
            res[i] = post * prefix[i]
            post = post * nums[i]

        return res

        


        