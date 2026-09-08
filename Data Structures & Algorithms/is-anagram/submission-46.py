class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        res = [1,2,3,4]
        res.sort()

        return sorted(s) == sorted(t)