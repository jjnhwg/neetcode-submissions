class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #stack will hold unresolved elements where we have not found the area whcih means we havent found 
        #a value that is smaller than the top of the stack 

        stack = []

    

        maxArea = 0 

        for i in range(len(heights) + 1):


            while stack and  (i  == len(heights) or heights[i] < heights[stack[-1]]): # while the new height we are adding is smaller than the top    
                index = stack.pop()

             
                
                height = heights[index]
                
        

                if stack:
                    width = i - 1 - stack[-1]
                else:
                    width = i


                maxArea = max(maxArea, height * width)
            
            stack.append(i)

        
        return maxArea




        