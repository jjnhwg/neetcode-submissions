class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Each element points to the next index we are going to 


        #1 4 3 2 2 


        slow, fast = 0, 0
        while True:
            slow = nums[slow] #slow is equal to the first element of the nums array so the element  
            fast = nums[nums[fast]] #fast is equal to the to the first element too? ur checking the if fast is element
                                    # u are checking the element at index 2 
            if slow == fast:
                break

        
        match = 0 

        while True:
            slow = nums[slow]
            match = nums[match]

            if slow == match:
                return slow
        
            

        
    
        


