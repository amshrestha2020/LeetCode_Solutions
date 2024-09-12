Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

 

Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105
 

Follow up: What if the number of rows is much larger than the number of columns?


from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(col):
            sums = [0] * row
            for right in range(left, col):
                for i in range(row):
                    sums[i] += matrix[i][right]
                arr = [0]
                cum = 0
                for sum in sums:
                    cum += sum
                    loc = bisect.bisect_left(arr, cum - k)
                    if loc < len(arr):
                        res = max(res, cum - arr[loc])
                    bisect.insort(arr, cum)
        return res

