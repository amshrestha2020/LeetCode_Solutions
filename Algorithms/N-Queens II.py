The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9



class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_place(pos, ocuppied_positions):
            for i in range(len(ocuppied_positions)):
                if ocuppied_positions[i] == pos or \
                    ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                    ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                    return False
            return True
        
        def place_queens(n, index, ocuppied_positions, count):
            if index == n:
                count[0] += 1
                return
            for i in range(n):
                if can_place(i, ocuppied_positions):
                    ocuppied_positions.append(i)
                    place_queens(n, index + 1, ocuppied_positions, count)
                    ocuppied_positions.pop()
        
        count = [0]
        place_queens(n, 0, [], count)
        return count[0]

