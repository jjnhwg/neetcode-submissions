class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        input is an array of nums, output of an array with arrays that result in the elements equaling to zero 
        where i need to find all the triplets or combinations of this array that equal to 0 

        [-1,0,1,2,-1,-4]

        [-4,-1,-1,0,1,2,]
        '''

        nums.sort()
        res = []

        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1 
            if i >= 1 and nums[i] == nums[i - 1]:
                continue 

            while l < r: 
                result = nums[i] + nums[l] + nums[r]

                if result > 0: 
                    r -= 1 
                elif result < 0:
                    l += 1 
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 
        
        return res
