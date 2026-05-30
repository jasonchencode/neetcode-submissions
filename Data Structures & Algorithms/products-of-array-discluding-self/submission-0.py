class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]
        pre.append(nums[0])
        for i in range(1, len(nums)-1):
            pre.append(nums[i] * pre[i])
        suf.append(nums[-1])
        temp = 1
        for j in range(len(nums)-2, 0, -1):
            suf.append(nums[j] * suf[temp])
            temp += 1
        returnlist = []
        for k in range(len(pre)):
            l = len(suf) - 1 - k
            returnlist.append(pre[k] * suf[l])
        return returnlist


        