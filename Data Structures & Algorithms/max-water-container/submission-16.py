class Solution:
    def maxArea(self, heights: List[int]) -> int:


        '''

        input: given a list of heights represented by numbers we need to output an integer that represents
        the max area that the containters will give 


        walkthough: using two pointers we can move inward to find if the bars are smaller than the widest one 

        to find the output then we would do r - l which is the width times the smaller bar to find the area 

        edge case: what if the two bars are not wide but they are very tall 

        what if the inner


        '''


        l, r = 0, len(heights) - 1 

        best = 0 

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            best = max(area, best)

            if heights[l] < heights[r]:
                l += 1 
            else:
                r -= 1 
            

        return best







        



        