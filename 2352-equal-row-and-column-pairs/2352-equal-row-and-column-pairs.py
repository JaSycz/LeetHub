class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dict = {}
        count = 0
        for row in grid:
            dict[str(row)] = dict.get(str(row),0)+1

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += dict.get(str(col),0)

        return count