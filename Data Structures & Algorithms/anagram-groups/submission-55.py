class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        input: array of strings 
        output: sublists of strings that are anagrams of each other 
        '''

        res = defaultdict(list)

        for word in strs:
            res[''.join(sorted(word))].append(word)

        return list(res.values())


        