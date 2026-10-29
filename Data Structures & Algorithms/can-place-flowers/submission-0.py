class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # brute force: go through array, counting how many times it's possible to:
        # - find 0, stop at it, if left 0 or out of bounds and right 0 or out of bounds, 
        # add to count
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if ((i-1 < 0) or flowerbed[i-1] == 0) and ((i+1 >= len(flowerbed) or flowerbed[i+1] == 0)):
                    count += 1
                    i += 1
            i += 1
        return count >= n