class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(len(nums)):
            num = nums[i]
            ans[i] = num
            ans[i+n] = num

        return ans
