class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [i]
            else: 
                hashmap[nums[i]].append(i)
                arr = hashmap[nums[i]]
                if arr[-1] - arr[-2] <= k:
                    return True
        return False