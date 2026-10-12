class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for word in strs:
            res += str(len(word)) + '#' + word
        
        return res


        "4#hello"


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1 
            number = int(s[i:j])
            i = j + 1
            res.append(s[i:i + number])
            i = i + number
        
        return res
        
        




            





