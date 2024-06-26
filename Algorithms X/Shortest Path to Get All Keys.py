You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

 

Example 1:


Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:


Input: grid = ["@Aa"]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'. 
There is exactly one '@' in the grid.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.





from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        all_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j, 0)
                elif 'a' <= grid[i][j] <= 'f':
                    all_keys |= (1 << (ord(grid[i][j]) - ord('a')))

        queue = deque([start])
        visited = set([start])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, keys = queue.popleft()
                if keys == all_keys:
                    return steps
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        cell = grid[nx][ny]
                        if cell == '#':
                            continue
                        new_keys = keys
                        if 'a' <= cell <= 'f':
                            new_keys |= (1 << (ord(cell) - ord('a')))
                        elif 'A' <= cell <= 'F' and not keys & (1 << (ord(cell) - ord('A'))):
                            continue
                        if (nx, ny, new_keys) not in visited:
                            queue.append((nx, ny, new_keys))
                            visited.add((nx, ny, new_keys))
            steps += 1

        return -1

