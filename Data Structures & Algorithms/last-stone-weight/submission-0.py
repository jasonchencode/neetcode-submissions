import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -(stones[i])
        heapq.heapify(stones)
        while len(stones) > 1:
            top = heapq.heappop(stones)
            if top == stones[0]:
                heapq.heappop(stones)
            else:
                second = heapq.heappop(stones)
                heapq.heappush(stones, top-second)

        if len(stones) == 0:
            return 0
        return abs(stones[0])