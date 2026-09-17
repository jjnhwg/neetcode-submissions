class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        '''
        given the input of a list of strings, the out should be a list of list of strings tha are grouped
        by anagram
        '''

        mp1 = defaultdict(list)

        for i in strs:
            mp1[''.join(sorted(i))].append(i)
        
        return list(mp1.values())
        