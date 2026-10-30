class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        input is a list of sorted numbers rotated and the output is the minimum of the array 

        we want to find in O(log(n)) - meaning binary search 

        walkthrough - condition for binary search 

        if nums[mid] < nums[r] then min is on the left side since mid < r that means there is a smaller number on the left    side     
        if nums[mid] > nums[r] then min is on the right side bc at a certain point it drops 

        '''

        #[3,4,5,6,1,2]
        #[1,2,3,4,5,6]
        


        l, r = 0, len(nums) - 1

        while l < r: 
            mid = (l + r) // 2 
            if nums[r] < nums[mid]:
                l = mid + 1 
            else: 
                r = mid
            
        return nums[l]

        


        