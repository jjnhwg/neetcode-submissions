class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        so given a number of arrays, and an element k return the 
        top k elemnts that show the most in the array 


        get the count of each elmeent in the nums and put 
        into a freq map 

        then given that freq map we want to put that into a 2d array 
        sort the array given the count of each elmeent
        and from the back we want to get the top k that shows up
        and use the other element in that 2d array 

    
        '''

        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)


        res = []

        for values, count in freq.items():
            res.append([count, values])

        res.sort()

        result = []


        while k > 0:
            result.append(res.pop()[1])
            k -= 1
    
        return result 
        






        
        