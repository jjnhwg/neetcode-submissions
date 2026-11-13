class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        mp = {}

        for i in range(len(nums)):
            mp[nums[i]] = 1 + mp.get(nums[i], 0)

        streak = 0



        for num in mp:
            if num - 1 in mp:
                continue 
            
            else:
                temp = 0 
                count = num
                print(count)
                while count in mp:
                    temp += 1 
                    count += 1
                
                
            streak = max(streak, temp)
                    
        
        return streak



        