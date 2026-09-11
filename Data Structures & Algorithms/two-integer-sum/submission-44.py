class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        diff = {}

        for i in range(len(nums)):
            minus = target - nums[i]

            if minus in diff:
                return [diff[minus], i]
            
            diff[nums[i]] = i