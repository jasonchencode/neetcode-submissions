class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        # bruteforce: check string s one letter at a time, and for each letter, we'd look at if it appears in there, and remove it from the string n^2
        # create a hashmap, and for each letter in string s, we would add it to the hashmap
        # for each letter in string t, we would check if the hashmap had that letter, and remove 1 for each time it appears, and at the end, we could check the max value in the hashmap because it would have to be 0
        hashmap = dict()

        for s_char in s:
            hashmap[s_char] = hashmap.get(s_char, 0) + 1
        
        for t_char in t:
            if t_char not in hashmap:
                return False
            hashmap[t_char] = hashmap[t_char] - 1
        if max(hashmap.values()) != 0:
            return False
        return True