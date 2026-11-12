class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        the input is a list of strings, the output is a 2d string in which its arrays of anagrams for each word 

        '''

        mp1 = defaultdict(list)

        for word in strs:

            sort = ''.join(sorted(word))
            mp1[sort].append(word)
        
        return list(mp1.values())