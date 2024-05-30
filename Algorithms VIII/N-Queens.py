The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9




class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check if there is a queen in the upper left diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check if there is a queen in the upper right diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def backtrack(board, row):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'
        
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return result
