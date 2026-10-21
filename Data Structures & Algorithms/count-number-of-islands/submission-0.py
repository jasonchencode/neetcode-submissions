class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def traverse(i, j):
            queue = deque([(i,j)])
            while queue:
                curri, currj = queue.popleft()
                if (curri, currj) not in visited:
                    visited.add((curri, currj))
                    for direction in directions:
                        nexti, nextj = curri + direction[0], currj + direction[1]
                        if 0 <= nexti < rows and 0 <= nextj < cols and grid[nexti][nextj] == "1":
                            queue.append((nexti, nextj))
                
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    traverse(i, j)
                    islands += 1
                    
        return islands