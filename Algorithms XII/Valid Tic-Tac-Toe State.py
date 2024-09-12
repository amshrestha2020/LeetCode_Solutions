Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
 

Example 1:


Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
Example 2:


Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
Example 3:


Input: board = ["XOX","O O","XOX"]
Output: true
 

Constraints:

board.length == 3
board[i].length == 3
board[i][j] is either 'X', 'O', or ' '.



from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        first, second = 'XO'
        x_count = sum(row.count(first) for row in board)
        o_count = sum(row.count(second) for row in board)
        if o_count not in {x_count-1, x_count}: return False
        if self.win(board, first) and x_count-1 != o_count: return False
        if self.win(board, second) and x_count != o_count: return False
        return True

    def win(self, board, player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)): return True
            if all(board[j][i] == player for j in range(3)): return True
        return board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player

