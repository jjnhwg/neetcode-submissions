class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        given input a list of strings, find the anagrams of each other, and then output a list of lists that are 
        grouped that are anagrams of each other 
        '''

        res = defaultdict(list)


        '''
        res = {}
        '''

        for i in strs:
            word = ''.join(sorted(i))
            res[word].append(i)
        
        return list(res.values())
        
        