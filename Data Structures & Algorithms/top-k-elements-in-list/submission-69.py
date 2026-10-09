class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #input: an array of nums and a k which represents how many elements we want to find
        #that show up 

        #output is the acc element that shows up the top most 



        #brute force would be to do adoubel for loop and make a count 
        


        cnt = {}

        for i in nums:
            cnt[i] = 1 + cnt.get(i, 0)
        
        sort = []

        for value, count in cnt.items():
            sort.append([count, value])
    

        sort.sort()

        res = []


        while k != 0:
            res.append(sort.pop()[1])
            k -= 1
        
        return res


