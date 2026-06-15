class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (high + low) // 2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][0] <= target and matrix[mid][-1] >= target: 
                break
            else:
                low = mid + 1
        i = mid
        low, high = 0, len(matrix[i])-1
        while low <= high:
            mid = (high + low) // 2
            if matrix[i][mid] > target:
                high = mid - 1
            elif matrix[i][mid] < target:
                low = mid + 1
            else:
                return True
        return False


