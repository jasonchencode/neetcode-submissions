class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # right off the bat, a brute force method for this could be create a dictionary of all letters, and check how long each string can go with for the k
        # i definitely think im going to be using a hashmap here
        # definitely using a sliding window
        # maybe even a queue here
        biggest = 0
        hashmap = dict()
        p1, p2 = 0, 0
        while p2 < len(s):
            hashmap[s[p2]] = hashmap.get(s[p2], 0) + 1
            if (p2 - p1+1) - max(hashmap.values()) > k:
                hashmap[s[p1]] -= 1
                p1 += 1
            biggest = max(biggest, p2 - p1+1) 
            p2 += 1
        return biggest
            

    





            