class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        smallest = high
        while low <= high:
            mid = (high+low)//2
            hours = 0
            i = 0
            while i < len(piles):
                if mid >= piles[i]:
                    hours += 1
                else:
                    hours += -(-piles[i] // mid )
                i += 1
            if hours <= h:
                smallest = mid
                high = mid - 1
            else:
                low = mid + 1
        return smallest


                
