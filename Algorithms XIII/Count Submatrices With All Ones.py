Given an m x n binary matrix mat, return the number of submatrices that have all ones.

 

Example 1:


Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:


Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
 

Constraints:

1 <= m, n <= 150
mat[i][j] is either 0 or 1.



class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(1, m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] += mat[i-1][j]
        res = 0
        for i in range(m):
            stack = []
            count = [0]*n
            for j in range(n):
                while stack and mat[i][stack[-1]] >= mat[i][j]:
                    stack.pop()
                if stack:
                    k = stack[-1]
                    count[j] += count[k] + mat[i][j]*(j-k)
                else:
                    count[j] += mat[i][j]*(j+1)
                stack.append(j)
            res += sum(count)
        return res
