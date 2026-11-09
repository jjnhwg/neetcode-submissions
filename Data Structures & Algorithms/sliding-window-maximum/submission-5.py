class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        q = deque()
        l = r = 0

        

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]: #q is the deque nums[q[-1]] is the last element and nums[r]
                #is the element that you just had added so basically just seeing if the back is less than 
                
                #waht you added and if so you pop and then you add

                q.pop()
            q.append(r)


            if l > q[0]:      
                q.popleft()  

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
            
          
        return res


