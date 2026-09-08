class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        use a hashmap for counting the numbers in the array, and then with that we can sort those numbers 
        with whatever was the highest count and then use a 2d array to get the acc element and then 
        return 
        
        '''

        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)


        values = []

        for val, count in freq.items():
            values.append([count, val])
        

        values.sort()
        res = []

        while k != 0:
            res.append(values.pop()[1])
            k -= 1
    
        return res







