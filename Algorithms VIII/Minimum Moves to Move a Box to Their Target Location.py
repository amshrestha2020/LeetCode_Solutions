A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

 

Example 1:


Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1
Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation: push the box down, left, left, up and up.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid contains only characters '.', '#', 'S', 'T', or 'B'.
There is only one character 'S', 'B', and 'T' in the grid.





from typing import List
from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Find the initial state
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    start_player = (i, j)
                elif grid[i][j] == 'B':
                    start_box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
        
        # Check if the player can reach a certain position without pushing the box
        def can_reach(player, box, target):
            visited = [[False]*n for _ in range(m)]
            visited[player[0]][player[1]] = True
            queue = deque([player])
            while queue:
                x, y = queue.popleft()
                if (x, y) == target:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != '#' and (nx, ny) != box:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            return False
        
        # BFS
        visited = set()
        queue = deque([(start_player, start_box)])
        visited.add((start_player, start_box))
        pushes = 0
        while queue:
            for _ in range(len(queue)):
                player, box = queue.popleft()
                if box == target:
                    return pushes
                for dx, dy in directions:
                    new_box = (box[0] + dx, box[1] + dy)
                    new_player = (box[0] - dx, box[1] - dy)
                    if 0 <= new_box[0] < m and 0 <= new_box[1] < n and grid[new_box[0]][new_box[1]] != '#' and can_reach(player, box, new_player):
                        if (new_player, new_box) not in visited:
                            queue.append((new_player, new_box))
                            visited.add((new_player, new_box))
            pushes += 1
        return -1
