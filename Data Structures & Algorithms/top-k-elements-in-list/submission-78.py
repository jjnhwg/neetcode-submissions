class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        given the input which is an array of nums return the k most amount of elmements that show up the most 
        return that in an array in any order 

        '''


        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        

        for key, value in freq.items():
            buckets[value].append(key)

        res = []

        for i in range(len(buckets) - 1, 0, -1):
            if k == 0:
                return res 
            
            for element in buckets[i]:
                res.append(element)
                k -= 1 
        
        return res
            




            
          
            

