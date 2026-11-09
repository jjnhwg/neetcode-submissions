class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        val = {}


        for i in range(k):
            val[nums[i]] = 1 + val.get(nums[i], 0)


        l, r = 0, k - 1 
        
        res = []

        while r < len(nums):
            res.append(max(val))
            r += 1

            val[nums[l]] -= 1 

            if val[nums[l]] == 0:
                del val[nums[l]]

            l += 1

            if r < len(nums):
                val[nums[r]] = 1 + val.get(nums[r], 0)
        
        return res


