class Solution:
    def findMin(self, nums: List[int]) -> int:


        '''
        input given is an array that has been rotated but it is in asending order and i need to find the smallest value


        [3,4,5,6,1,2]

        [1,2,3,4,5,6]
        
        '''

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid  
            elif nums[mid] < nums[r]:
                r = mid 

            if (r - l) == 1:
                return min(nums[l], nums[r])
        
        return nums[l]
                








