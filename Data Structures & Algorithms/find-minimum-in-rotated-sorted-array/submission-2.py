class Solution:
    def findMin(self, nums: List[int]) -> int:
        # using binary search

        # low = 3, high = 2
        # if high > low, return low
        # otherwise, go to mid, if mid > high, reset mid, continue until you found the lowest num 
        low, high = 0, len(nums)-1
        if nums[high] > nums[low]:
            return nums[low]
        while low < high:
            mid = (low + high) // 2
            if nums[high] > nums[mid]:
                high = mid 
            else:
                low = mid + 1
        return min(nums[low], nums[high])


