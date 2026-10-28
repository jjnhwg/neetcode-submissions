class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        input is the prices one each day and the output is the max profit from those days ordered
        w the later day being the one from subtracted from

 
        '''

        l, r = 0, 1 #parking lot: length = 1 

        profit = 0
        
        while r < len(prices):

            while prices[r] < prices[l]:
                l = r 
                r = r + 1 
    
                if r >= len(prices):
                    return profit

            profit = max(prices[r] - prices[l], profit)

            r += 1

        
        return profit 
            


            


