class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()
        for char in s:     
            hashmap[char] = hashmap.get(char, 0) + 1
        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
        if max(hashmap.values()) != 0:
            return False
        return True

            