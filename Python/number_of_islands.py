"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Go through every element,
        When we find an island, recursively set its neighbor grid as 0 if there is a 
        land too. In other word, when we meet 1, It should the start of an island,
        then we should not meet another "1" if it is connected to the same lsland,
        becuase we set it "0", So we just need to count how many times "1" we meet.
        """
        def remove_neighbor(i, j):
            grid[i][j] = "0"
            # up
            if i > 0 and grid[i-1][j] == "1":
                remove_neighbor(i-1, j)
            # down
            if i + 1 < len(grid) and grid[i+1][j] == "1":
                remove_neighbor(i+1, j)
            # left
            if j > 0 and grid[i][j-1] == "1":
                remove_neighbor(i, j-1)
            # right
            if j + 1 < len(grid[i]) and grid[i][j+1] == "1":
                remove_neighbor(i, j+1)

        if not grid:
            return 0

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    island_count += 1
                    remove_neighbor(i, j)

        return island_count
