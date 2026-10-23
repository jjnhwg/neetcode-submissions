class Solution:
    '''

    5#Hello5#World
    '''

    def encode(self, strs: List[str]) -> str:
        empty_str = []

        for word in strs:
            empty_str.append(str(len(word)) + "#" + word) 
        
        return ''.join(empty_str)


    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        while i < len(s):
            l = i 
            while s[l] != "#":
                l += 1 
            
            number = int(s[i:l])
            begin = l + 1

            word = s[begin: begin + number]
            res.append(word)
            i = begin + number
    
        return res 
         

            






