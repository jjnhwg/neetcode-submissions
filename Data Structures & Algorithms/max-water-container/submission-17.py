class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        input an array of ints representing bars 
        output the max area of the bars 

        problem walkthrough 

        '''

        l , r = 0, len(heights) - 1

        best = 0 

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            best = max(area,best)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1 
        
        return best