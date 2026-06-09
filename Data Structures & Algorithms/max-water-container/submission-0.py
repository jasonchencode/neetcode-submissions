class Solution:
    def maxArea(self, heights: List[int]) -> int:
        top2 = []
        p1, p2 = 0, len(heights)-1
        max = 0
        while p1 != p2:
            if heights[p1] < heights[p2]:
                new_max = heights[p1] * (p2-p1)
                p1 += 1
            elif heights[p1] > heights[p2]:
                new_max = heights[p2] * (p2-p1)
                p2 -= 1
            else:
                new_max = heights[p1] * (p2-p1)
                p1 += 1
            if new_max > max:
                max = new_max
        return max