class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else: 
                maxi = max(maxi, count)
                count = 0
            i += 1
        maxi = max(maxi, count)
        return maxi