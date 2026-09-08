class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mp = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            print('hit')
            if diff in mp:
                print('hit')
                return [mp[diff],i]
            
            mp[nums[i]] = i 

        