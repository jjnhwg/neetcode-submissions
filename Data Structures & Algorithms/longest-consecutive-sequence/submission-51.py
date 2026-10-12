class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:               # <- the fix
            return 0

        nums.sort()
        streak = 1
        maxStreak = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue                       # duplicate: don't break or extend the streak
            elif nums[i] + 1 == nums[i + 1]:
                streak += 1                    # consecutive: extend
            else:
                streak = 1                     # gap: reset
            maxStreak = max(streak, maxStreak)

        return maxStreak

# TRACE: nums = [1, 2, 0, 1]  -> sorted [0, 1, 1, 2]   (expected: 3)
#
# i=0 | 0 vs 1 | 0+1==1 consecutive | streak=2 | max=2
# i=1 | 1 vs 1 | duplicate, skip    | streak=2 | max=2
# i=2 | 1 vs 2 | 1+1==2 consecutive | streak=3 | max=3
# return 3 ✓
#
# TRACE: nums = []   (expected: 0)
# old code: loop never runs -> returns 1 ✗
# new code: hits `if not nums` -> returns 0 ✓