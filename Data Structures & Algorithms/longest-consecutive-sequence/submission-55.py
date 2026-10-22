class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        '''
        input is an array of numbers with the output being the 
        the amount of elements that are consecutive in this array 

        sorting it but that would be n log n 


        if i - 1 not in 



        '''

        numbers = set(nums)

        longest = 0

        for i in numbers:
            if i - 1 not in numbers:
                count = 0
                while i in numbers:
                    count += 1 
                    i += 1 
                
                longest = max(longest, count)
            
        return longest 






        


        