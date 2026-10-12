class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #edge case: no need to repeat elements that are already in that streak 
        #edge case: loop trhoguh until we dont find the next additional value

        numSet = set(nums)

        longest = 0





        for num in numSet:

            if (num - 1) not in numSet:
                length = 1 
                while (num + length) in numSet:
                    length += 1 
                
                longest = max(length, longest)
        
        return longest

        


