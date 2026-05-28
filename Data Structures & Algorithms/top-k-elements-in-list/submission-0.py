class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = set()
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            if len(output) < k:
                output.add(nums[i])
            elif nums[i] not in output:
                for n in output:
                    if hashmap[nums[i]] > hashmap[n]:
                        output.remove(n)
                        output.add(nums[i])
                        break
        return list(output)

        