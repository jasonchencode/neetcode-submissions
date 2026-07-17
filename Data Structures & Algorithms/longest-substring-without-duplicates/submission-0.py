class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest = 0
        hashmap = dict()
        p1 = 0
        for p2, num in enumerate(s):
            if num in hashmap and hashmap[num] >= p1:
                p1 = hashmap[num] + 1

            hashmap[num] = p2
            biggest = max(biggest, p2 - p1 + 1)
        return biggest



