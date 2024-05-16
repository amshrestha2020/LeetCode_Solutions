Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105




class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m + n)]
        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])
        result = []
        for i, diagonal in enumerate(diagonals):
            if i % 2 == 0:
                result.extend(diagonal[::-1])  # reverse the diagonal
            else:
                result.extend(diagonal)
        return result
