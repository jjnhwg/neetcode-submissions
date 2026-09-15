class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        input given is an array o fnums 
        and k which is the amount of numbers we want to see that show up the most in this array
        return len(k) of nums



        you can put the elements that are in the highest in an array where each array is 1 -indexed and it rep
        resents how many times it shows up in the array 

        at most the numbers will show up is the len(nums)


        '''

        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        res = []

        for i in range(len(nums) + 1):
            res.append([])

        for value, cnt in count.items():
            res[cnt].append(value)
        
        result = []

        for i in range(len(res) - 1, 0, -1):
            for num in res[i]:
                result.append(num)
                if len(result) == k:
                    return result
        


        