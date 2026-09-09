class Solution:

    '''
    given an input a list of strings, we want to turn that into one string, and using that one 
    string we want to be able to get back that orignal array of strings






    [hello, world]

    hello;world


    '''
    def encode(self, strs: List[str]) -> str:

        empty_str = ""

        for word in strs:
            formatted_word = str(len(word)) + '#' + word 
            empty_str += formatted_word


        return empty_str


    def decode(self, s: str) -> List[str]:

        "5#hello5#world"

        res = []
        l, r = 0, 0 

        while l < len(s):

            while s[r] != '#':
                r += 1

            number = int(s[l:r])
            l = r + 1
            
            res.append(s[l:l + number])

            l = l + number
            r = l

    
        return res


        


            


            


     




