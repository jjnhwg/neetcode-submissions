class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        given an array of integers each element represnts the number of bananas in that pile 
        h - the amount of hours you have to be able to eat all the banaas 

        ^inputs 

        return the lowest rate of bananas you can eat per hour 


        #[1,4,3,2], h = 9

        Important things - if the len(piles) = h then the output has to be the max of piles because 
        you dont have any more hours to allocate to eat less then the max of your array 
 
        '''

        l, r, = 1, max(piles)

        res = r


        while l <= r:

            mid = (l + r) // 2 

            hours = 0 

            for p in piles:
                hours += math.ceil(float(p) / mid)
                

            if hours <= h:

                res = min(res, mid)

                r = mid - 1 
            
            else:
                l = mid + 1 
        
        return res




