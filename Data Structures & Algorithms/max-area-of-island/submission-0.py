class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # queue
        # set for nodes that we've already visited

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        max_island = 0

        def bfs(i, j):
            queue = deque([(i,j)])
            island = 0
            while queue:
                curri, currj = queue.popleft() 
                if (curri, currj) not in visited:
                    visited.add((curri, currj))
                    island += 1
                    for direction in directions:
                        nexti, nextj = curri + direction[0], currj + direction[1]
                        if 0 <= nexti < rows and 0 <= nextj < cols and grid[nexti][nextj] == 1:
                            queue.append((nexti, nextj))
            return island
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_island = max(max_island, bfs(i,j))
        return max_island


        

