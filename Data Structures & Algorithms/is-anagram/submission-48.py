class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        mp1 = {}
        mp2 = {}


        for i in s:
            mp1[i] = 1 + mp1.get(i,0)
        

        for j in t:
            mp2[j] = 1 + mp2.get(j,0)




        return mp1 == mp2 