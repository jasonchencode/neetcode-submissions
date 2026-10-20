class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # First glance, we would use a hashmap
        nums.sort()
        i = len(nums) // 2
        return nums[i]
