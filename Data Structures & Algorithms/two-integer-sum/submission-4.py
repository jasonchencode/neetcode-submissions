class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = []
            hashmap[nums[i]].append(i)
        for num in hashmap:
            diff = target - num
            if diff in hashmap:
                if diff == num and len(hashmap[diff]) == 1:
                    continue
                if hashmap[num][0] < hashmap[diff][0]:
                    return [hashmap[num][0], hashmap[diff][0]]
                returnlist = [hashmap[diff][0]]
                hashmap[diff].pop(0)
                returnlist.append(hashmap[num][0])
                return returnlist


        