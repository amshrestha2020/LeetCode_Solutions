Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.



class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_less_equal(matrix, mid, smaller, larger):
            count, n = 0, len(matrix)
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    # As matrix[row][col] is bigger than the mid, let's keep track of the
                    # smallest number greater than the mid
                    larger[0] = min(larger[0], matrix[row][col])
                    row -= 1
                else:
                    # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                    # biggest number less than or equal to the mid
                    smaller[0] = max(smaller[0], matrix[row][col])
                    count += row + 1
                    col += 1

            return count

        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = [start], [end]
            count = count_less_equal(matrix, mid, smaller, larger)

            if count == k:
                return smaller[0]
            if count < k:
                start = larger[0]  # search higher
            else:
                end = smaller[0]  # search lower

        return start
