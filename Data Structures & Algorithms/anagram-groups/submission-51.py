class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        probelm given is i am given an array of strings and 
        my output is return 2d array, of anagrams of the strings given 
        in taht 2d array.

    1. brute force method 
    2. why brute force too slow 
    3. what pattern do i notice 
    4. what data structure solves that problem 
    5. what is the complexity
        '''

        '''

        '''

        res = defaultdict(list)

        for i in strs:
            res[''.join(sorted(i))].append(i)



        return list(res.values())

  


       
        