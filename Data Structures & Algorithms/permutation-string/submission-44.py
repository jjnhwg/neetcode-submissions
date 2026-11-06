class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        the inputs that i am given are s1 and s2 and i return true if a perumation is in s2 

        brute force: doubee for loop add to a map check to see if tha tmpa euals to what s2 map eausl to 

        '''



        match = {}
        curr = {}

        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            match[s1[i]] = 1 + match.get(s1[i], 0)
            curr[s2[i]] = 1 + curr.get(s2[i], 0)


        l, r = 0, len(s1) - 1 

        while r < len(s2):
            if match == curr:
                return True
            
            else:
                curr[s2[l]] -= 1
                if curr[s2[l]] == 0:
                    del curr[s2[l]]
                
                
                r += 1 

                if r == len(s2):
                    return False

                l += 1 

                curr[s2[r]] = 1 + curr.get(s2[r], 0)

        
        return False
                


        

        
        