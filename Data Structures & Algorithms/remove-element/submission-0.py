class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # brute force method: 
        # create a new list of everything that's not equal to the value
        p1, p2 = 0, len(nums)-1
        counter = 0
        while p1 <= p2:
            if nums[p1] == val:
                temp = nums[p2]
                nums[p2] = nums[p1]
                nums[p1] = temp
                p2 -= 1
            else:
                counter += 1
                p1 += 1
        return counter