class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        given an input array of nums

        '''

        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)


        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        
        for value, cnt in freq.items():
            bucket[cnt].append(value)

        res = []

        for i in range(len(bucket) -1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        return res

        

