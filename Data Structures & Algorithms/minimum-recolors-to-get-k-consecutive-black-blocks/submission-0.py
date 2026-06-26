class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        p1, p2 = 0, 0
        outputBs = 0
        maxBs = 0
        while p2 < len(blocks):
            if blocks[p2] == 'B':
                outputBs += 1
            if maxBs < outputBs:
                maxBs = outputBs
            
            if p2 - p1 < k - 1:
                p2 += 1
            else:
                if blocks[p1] == 'B':
                    outputBs -= 1
                p1 += 1
                p2 += 1
        return k - maxBs
                

        # go through entire array
        # window expands until p2 - p1 >=  k - 1
        # keep track of Bs