class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
        input array of nums
        output : array of nums that are multiplied with each other exepcet for the elemnt/index of the array
        that we are on
        '''


        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre = nums[i] * pre


        #[1,2,4,6]

        #[1,1,2,8]
        #[48,24,6,1]

        #[48,24,12,8]

        post = 1 

        for i in range(len(nums) - 1, -1, -1):
            res[i] = post * res[i]
            post = post * nums[i]

        return res

        


        