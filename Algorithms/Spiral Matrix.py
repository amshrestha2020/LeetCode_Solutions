Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100




class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            # Add the first row
            result += matrix.pop(0)
            # Add the last element of each remaining row
            result += [row.pop() for row in matrix if row]
            # Add the last row (reversed)
            if matrix:
                result += matrix.pop()[::-1]
            # Add the first element of each remaining row (reversed)
            result += [row.pop(0) for row in matrix[::-1] if row]
        return result

