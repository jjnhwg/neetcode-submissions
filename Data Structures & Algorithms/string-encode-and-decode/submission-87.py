class Solution:

    def encode(self, strs: List[str]) -> str:

        decode = []
        for word in strs:
            decode.append(str(len(word)) + '#' + word) #
        return ''.join(decode)
        

    def decode(self, s: str) -> List[str]:

        l, r = 0, 0 
        res = []

        4#word
        
        while r < len(s):


            while s[r] != '#':
                r += 1 
            
            count = int(s[l:r])

            l = r + 1 

            word = s[l:l + count]

            res.append(word)

            l = l + count
            r = l 

        return res