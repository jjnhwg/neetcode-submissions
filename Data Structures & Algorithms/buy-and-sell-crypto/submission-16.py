class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        given input array of integer of priees
        return an integer where its the max profit of those prices when doing r - l

        '''

        l, r = 0, 1 

        res = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r 
                r += 1 
            
            else:
                res = max(res, prices[r] - prices[l])
                r += 1

        
        return res

            

