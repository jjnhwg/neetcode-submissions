class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        input is a string and the output is the length of the substring w/o any duplicates

        we can use a set and do two pointers and add elements to the set, as we move the right pointer
        if we encounter an element already in the set we can remove from the left until we 
        find that dupliecates and remove it and then restart the length count 

        more efficent way is to not have to loop through until we remove that left elmeent what we cand o instead 
        is have a hash map the values being the index and we jump to the index and then count the length from there
        but also making sure that the 

        '''
        # zxyzxyz
        #aa
        
        mp1 = {}
        res = 0

        l, r = 0, 0
        #edge case being if the element is 1 

        while r < len(s):
            if s[r] in mp1 and mp1[s[r]] >= l: #
                l = mp1[s[r]] + 1
                mp1[s[r]] = r
            else:
                mp1[s[r]] = r

            res = max(res, (r - l) + 1)
            r += 1
    
        return res




        