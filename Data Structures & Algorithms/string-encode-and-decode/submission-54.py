class Solution:

    #questions to ask why this causes empty_strs += str(len(i)) + "#" + i

    '''
    given a list of input strings, encode and then using another method decode that same string
    '''

    def encode(self, strs: List[str]) -> str:
        res = []

        for i in strs:
            res.append(str(len(i)) + "#" + i)
        
        return ''.join(res)


    def decode(self, s: str) -> List[str]:

        4#hello

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


        

        



        
