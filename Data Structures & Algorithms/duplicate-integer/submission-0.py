class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        i = 0
        while i < len(nums):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
            i += 1
        return False