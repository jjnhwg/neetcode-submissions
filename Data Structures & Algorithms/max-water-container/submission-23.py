class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''
        input - an integer of heights representing bars
        output - the area from the heights and the max area 

        brute force: double for loop check combinations to see which gives the biggest area

        walkthorugh: 
        '''

        l, r = 0, len(heights) - 1 

        res = 0

        while l < r: 
            res = max(res, min(heights[l], heights[r]) * (r - l))

            if heights[l] < heights[r]:
                l += 1 
            else: 
                r -= 1 
        
        return res








        