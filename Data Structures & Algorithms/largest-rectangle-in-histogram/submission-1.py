class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1): #loop 1 extra in your loop and start from zero 

            while stack and (i == n  or heights[stack[-1]] >= heights[i]): # while there is a stack if not then we are appendin gthe first element 
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea


        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(len(heights)):

            while stack and heights[i] < stack[-1]:
                height = heights[stack.pop()]

                if not stack:
                    width = i 
                else:
                    width = i - stack[-1] - 1
                
                maxArea = max(maxArea, height + width)
            


            stack.append(i)
        
        return maxArea 



            





