class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
        input is an array of nums, and the target number in which you are trying to find 
        the output is a target index which finds the number that we are looking for 
        '''

        l, r = 0, len(nums) - 1

        while l <= r:
            
            mid = (r + l) // 2
            
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1 
            else:
                return mid
        
        return -1 







        



        