class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        inputs are a list of numbers and a target and the target represents what index from the list of numbers
        will add to that target 


        output the list of number indexes that will add to that target 
        '''


        l, r = 0, len(numbers) - 1 

        while l < r:
            add = numbers[l] + numbers[r]

            if add == target:
                return [l + 1, r + 1]

            if add < target:
                l += 1
            else:
                r -= 1 
        
        

            



        