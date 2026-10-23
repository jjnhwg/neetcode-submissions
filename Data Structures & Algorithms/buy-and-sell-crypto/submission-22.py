class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        input is an array of prices of specific days in which the output is the max profit from with those days we can 

        '''

        l, r = 0, 1
        res = 0

        while r < len(prices):

            if prices[r] < prices[l]:
                l = r 
                r = r + 1

                if r >= len(prices):
                    return res
            

            res = max(prices[r] - prices[l], res)
            r += 1 
    
        
        return res
            



