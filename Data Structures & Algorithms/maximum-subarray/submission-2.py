class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # almost sliding window
        # reject negative values, keep same max
        # use two pointers
        p1, p2 = 0, 1
        globalmax = maxval = nums[p1]
        while p2 < len(nums):
            if maxval < 0 and maxval < nums[p2]:
                p1 = p2
                maxval = nums[p2]
            else: 
                maxval = maxval + nums[p2]
            globalmax = max(maxval, globalmax)
            p2 += 1
        return globalmax
