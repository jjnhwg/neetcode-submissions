class Solution:

    '''
    we are given a string to encode and two methods to encode that string so that the decoder can decode it

    '''

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i)) + "#" + i)
    
        return ''.join(res)



    def decode(self, s: str) -> List[str]:

        print(s)

        "4#hello"

        res = []

        l, r = 0,0 

        while l < len(s):
   
            while s[r] != '#':
                r += 1 
            
            number = int(s[l:r])

            l = r + 1 

            res.append(s[l:number + l])


            l = number + l
            r = l
        
        return res


