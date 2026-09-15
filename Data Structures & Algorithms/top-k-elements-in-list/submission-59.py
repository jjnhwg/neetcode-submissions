class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        input given is an array o fnums 
        and k which is the amount of numbers we want to see that show up the most in this array
        return len(k) of nums
        '''

        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        source = []

        for value, cnt in count.items():
            source.append([cnt, value])
        
        source.sort()


        res = []

        while len(res) < k:
            res.append(source.pop()[1])
        
        return res



        