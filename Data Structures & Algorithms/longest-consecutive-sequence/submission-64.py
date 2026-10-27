class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #parking lot items 
        #what is the brute force 

        '''
        the input is an array of numbers and the output is the length of a consecuvie sequence how long 
        that could be 
        '''

        numbers = set(nums)

        length = 0

        for i in numbers:
            if i - 1 not in numbers:
                count = 0 
                j = i 
                while j in numbers:
                    count += 1
                    j += 1 
                
                length = max(count, length)
        
        return length
                



        