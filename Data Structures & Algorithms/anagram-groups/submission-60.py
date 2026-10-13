class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        input - an array of strings 
        output - a 2d array where each array in the array are anagrams of each other from the origanal array 
        '''

        res = defaultdict(list)

        for word in strs:
           sorted_word = ''.join(sorted(word))
           res[sorted_word].append(word)
        
        return list(res.values())


        
        