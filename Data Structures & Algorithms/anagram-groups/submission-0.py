class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            alphabet = [0] * 26

            for char in string: 
                alphabet[ord(char) - ord("a")] += 1
            
            hashmap[tuple(alphabet)].append(string)

        return list(hashmap.values())