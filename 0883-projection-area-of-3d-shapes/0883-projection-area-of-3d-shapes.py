class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        area = 0

        # XY projection: count non-zero cells
        for row in grid:
            for val in row:
                if val > 0:
                    area += 1

        # YZ projection: maximum of each row
        for row in grid:
            area += max(row)

        # XZ projection: maximum of each column
        for col in range(n):
            area += max(grid[row][col] for row in range(n))

        return area